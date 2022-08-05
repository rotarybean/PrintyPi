#------------@section Modules------------
from main import boxnum, bppart, cpart, pdesc, qbox, color, mater, monum, tbox, lotstr
import os
from PIL import Image, ImageDraw, ImageFont

#------------@section Objects------------
template = Image.open('./resources/ltemplatev2.jpg')
fill = ImageDraw.Draw(template)
lbig = ImageFont.truetype('./resources/SANSSERIF.TTF', 60)
lsmall = ImageFont.truetype('./resources/SANSSERIF.TTF', 40)
output = "./resources/label.%s"
topdf = Image.open("./resources/fielded.jpg")
convert = topdf.convert('L')
pdf_filename = output % ("pdf")


#------------@section Action-------------
def print():
    fill.text((489, 105), bppart, font=lbig, fill=(0, 0, 0)) #16 Digit Part Number
    fill.text((45, 250), cpart, font=lsmall, fill=(0, 0, 0)) # Customer Part Number
    fill.text((380, 244), pdesc, font=lsmall, fill=(0, 0, 0)) # Part Description
    fill.text((885, 244), qbox, font=lsmall, fill=(0, 0, 0)) # Box Quantity
    fill.text((26, 371), color, font=lsmall, fill=(0, 0, 0)) # Colorant
    fill.text((379, 371), mater, font=lsmall, fill=(0, 0, 0)) # Material
    fill.text((510, 490), monum, font=lsmall, fill=(0, 0, 0)) # MO Number
    fill.text((798, 490), lotstr, font=lsmall, fill=(0, 0, 0)) # Generated Lot Number
    fill.text((125, 490), boxnum+" of "+tbox, font=lsmall, fill=(0, 0, 0)) # Current box number
    template.save("fielded.jpg")
    convert.save(pdf_filename)
    os.system("lp %s" % "./resources/label.pdf")