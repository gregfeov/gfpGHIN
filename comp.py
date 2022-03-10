from gfplib import *
from co import *
import os
import time
from ert import *
def vf(na,pae,a,se,fe):
    pa = conne(na)
    if pa == False:
        print("Can't find user with that name!\nPlease try again!")
        a.set("Can't find user with that name!\nPlease try again!")
        return False
    # print(delchar(pa))
    if pae == pa:
        print("Successful")
        a.set("Successful")
        se.config(bg="#242424", fg="#15ff00",font=(6))
        return True
    else:
        print("Incorrect password")
        a.set("Incorrect password")
        return False
