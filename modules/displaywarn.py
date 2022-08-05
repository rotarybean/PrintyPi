#------------@section Modules-------------
from PIL import Image, ImageDraw, ImageFont
import time
import spidev as SPI
import LCD_2inch
import lcdconfig
from modules import display

#------------@section Pins----------------
RST = 27
DC = 25
BL = 18
bus = 0
device = 0

#------------@section Objects-------------
disp = LCD_2inch.LCD_2inch()
warn = Image.new("RGB", (disp.height, disp.width ), "RED")
draw = ImageDraw.Draw(warn)
font = ImageFont.tryetype("./resources/ZIG.TTF", 60)

#------------@section Action--------------
def displaywarn():
    disp.Init()
    disp.clear()
    draw.text((60, 68), 'WARNING', fill = "BLACK",font=font)
    draw.text((30, 128), 'NEW ORDER', fill = "BLACK",font=font)
    disp.ShowImage(warn)
    time.sleep(1)
    disp.clear()
    disp.ShowImage(warn)
    time.sleep(1)
    disp.clear()
    disp.ShowImage(warn)
    time.sleep(1)
    disp.clear()
    display()
    disp.module_exit()