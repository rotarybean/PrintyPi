# PrintyPi for Press
# This code is designed to receive and display label information on standalone units mounted to label printers at each injection molding press.
# Production workers will press a single button to print a generated label for boxes.  Management will have the ability to update label information
# for each press printer by accessing a locally hosted webpage containing a PHP form which sends form data to the Python script, which will in turn
# be applied to the labels.
#
# This is an overhaul, switching to a multi-module system from a flat file.  Overhaul performed 8/4/2022.
#
# Order of Operations:
#   Apache-hosted HTML file displays PHP with $POST and $GET form data from JSON
#   database. Display will be GUI with multiple elements:
#       "Submit New Order" will be a left-aligned alphanumeric 9-value form, but not all values
#           will be used by 'main.py'.  Part Number field will be drop-down with 
#           predefined values of known BP designated part numbers and an option to add
#           a new BP designated part number, but will require fresh data in all fields.
#           Consider adding Stock Order checkbox to indicate.
#           Submission will add the order next-in-line.
#       "Current Order" will be right-aligned and consist of a column of values in the current
#           production queue.  List values will be $GET (make live if possible, no refresh) and
#           consist of BP Part Number, Customer Part Number, Part Description, Quantity/box, 
#           MO number, generated Lot Number, Current Box Number, and average time between boxes(production rate)(?).
#       -Separator Bar Here-
#       "Print Queue" header text centered, two columns of print queues.  Each job in queue will 
#           be numbered according to their position in the queue.  Add Make Current and Make First
#           buttons on each order in queue.  Jobs will contain same values as "Current Order".
#
#   'main.py' 
#       This file.  Pulls form data from current order, calculates lotstring and boxnum, then submits 
#       all label data to database, print.py module and display.py module.
#   'print.py' is a module.  It calls values predefined by 'main.py', PILLOW, and ltemplatev2.jpg, 
#       draws text onto image, and submits it to os.lp to send to printer. 
#   'display.py' is a module.  The LCD stays off until buttonEvent, at which point it calls values
#       from 'main.py' and displays the data on the screen.  After 30 seconds, the display powers off
#       to prevent burn-in.  Add if boxnum = tbox, flash screen red and alert operator of new order, start new pallet.
#       Background is semi-transparent BP blue logo, SANSSERIF.TTF is value font.  Display values only with emphasis
#       (bold or larger text) on bppart, monum, boxnum, and tbox. 
#  
# Creator: @rotarybean for Barrett Plastics
# Project Started 7/1/2022, overhauled 8/4/2022
# version alpha v0.16

#------------@section Modules-------------
import os
import math
from datetime import date
import time
import RPi.GPIO as GPIO
from modules import print
from modules import display
from modules import terminal
from modules import displaywarn


#------------@section Variables-----------
todays_date = date.today()
year = todays_date.strftime("%y") # 2 digit year
week = todays_date.strftime("%V") # 2 digit week
press = 1
boxnum = 1
bppart = "STR06WHT99015"
cpart = "Iridium"
pdesc = "White Snip Tip"
qbox = "15000"
color = "Wht 99015"
mater = "PP1635"
monum = "2043"
ordeq = "65000"
tbox = (math.ceil( float(ordeq)/float(qbox)))
lotstr = str(year)+str(week)+str(press).zfill(2)+str(monum)

#------------@section Setup--------------
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#------------@section Action-------------
def buttonEvent(channel):
    boxnum + 1
    print()
    display()
    terminal()
    
    if boxnum >=tbox:
        time.sleep(3)
        displaywarn()
        print("M.O. Complete!  Preparing. . .")
        boxnum = 0
        time.sleep(3)
        os.system('clear')
        print("Ready!")

#------------@section Loop---------------
def loop():
    GPIO.add_event_detect(22, GPIO.FALLING, callback = buttonEvent, bouncetime=3000) #Do buttonEvent when buttonpress detected, set to 3 seconds to account for bounce and printer timing
    while True:
        pass

def destroy():
    GPIO.cleanup()

if __name__ == '__main__' :
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()