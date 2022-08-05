#------------@section Modules-------------
from main import boxnum, bppart, pdesc, qbox, color, mater, tbox, lotstr
from PIL import Image, ImageDraw, ImageFont
import time
import spidev as SPI
from resources import LCD_2inch
from resources import lcdconfig

#------------@section Pins----------------
RST = 27
DC = 25
BL = 18
bus = 0
device = 0

#------------@section Objects-------------
disp = LCD_2inch.LCD_2inch()
background = Image.open('./resources/background.jpg')
draw = ImageDraw.Draw(background)
background = Image.rotate(180)
big = ImageFont.truetype("./resources/SANSSERIF.TTF",30)
small = ImageFont.truetype("./resources/SANSSERIF.TTF", 15)

#------------@section Action----------------
def display():
    disp.Init()
    disp.clear()
    disp.ShowImage(background)
    draw.text((5, 2), bppart, fill = "BLACK",font=big)
    draw.text((5, 32), pdesc, fill = "BLACK", font=small)
    draw.text((5, 62), 'Quantity/Box: '+qbox, fill = "BLACK",font=small)
    draw.text((5, 92), 'Colorant: '+color, fill = "BLACK",font=small)
    draw.text((5, 122), 'Material: '+mater, fill = "BLACK",font=small)
    draw.text((5, 152), 'Lot#: '+lotstr, fill = "BLACK",font=small)
    draw.text((5, 192), 'Box#: '+boxnum+' of '+tbox, fill = "BLACK",font=big)
    time.sleep(3)
    disp.module_exit()