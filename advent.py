import time
import random
import board
import neopixel
import random
from ncount import *
from prt import *
from wise import *
from intput import *


radius = 3
map = "ship.adv"

def loc(x,y):
    l = x + (y*radius)
    return l

px = 1
py = 1

def where(x,y): #return location text based on location
    loctxt = wisdom(loc(x,y),map)
    return loctxt

def chgloc(dir): #change location
    global px
    global py
    if dir == "n":
        py = py - 1
        if py < 0:
            py = 0
    if dir == "s":
        py = py + 1
        if py >= radius:
            py = radius - 1
    if dir == "w":
        px = px - 1
        if px < 0:
            px = 0
    if dir == "e":
        px = px + 1
        if px >= radius:
            px = radius - 1


compthink()

REPL = True

if REPL == False:
    Val=0
    while Val==0:
        blinknum(1,red)
        if touch1.value:
            Val = Val + 1
        if touch2.value:
            Val = Val + 2

prt("you are in "+where(px,py),REPL)

while True:
    prt("where do you want to go? NSEW?",REPL)

    dir = intpt("nsew",REPL)
    compthink()
    chgloc(dir)

    prt("you are in "+where(px,py),REPL)


