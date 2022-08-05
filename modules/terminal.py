#------------@section Modules------------
from main import press, boxnum, bppart, cpart, pdesc, qbox, color, mater, monum, tbox, lotstr
import os

#------------@section Action-------------
def terminal():
    os.system('clear')
    print("Press #: ",press)
    print("BP Part #: ",bppart)
    print("Customer Part #: ",cpart)
    print("Description: ",pdesc)
    print("Quantity/Box: ",qbox)
    print("Color: ",color)
    print("Material: ",mater)
    print("M.O. #: ",monum)
    print("Lot #: ",lotstr)
    print("Box #: ",boxnum," of ",tbox)