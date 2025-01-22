import time
import random
import board
import neopixel
from ncount import *
from prt import *
from wise import *
from intput import *

# important: set radius to define size of map. set map to the file of room descriptions
radius = 3 # change to width of A x A matrix of rooms. 
map = "ship.adv"  #change to file listing rooms for adventure

WRAP = False # True for a 'torus' map, False for non-torus

 
def loc(x,y):
    l = x + (y*radius)
    return l

px = 1 #set to starting room X position
py = 1 #set to starting room Y position

def where(x,y): #return location text based on location
    loctxt = wisdom(loc(x,y),map)
    loctxt.strip("\n")
    l= loctxt.split("|")
    if len(l)==2:
        return (l[0],l[1])
    else:
        return (l[0],"nsew")
        
def chgloc(dir): #change location 
    global px
    global py
    if dir == "n":
        py = py - 1
    if dir == "s":
        py = py + 1
    if dir == "w":
        px = px - 1
    if dir == "e":
        px = px + 1
    if WRAP:
        if px < 0:
            px = radius - 1
        if px >= radius:
            px = 0
        if py < 0:
            py = radius - 1
        if py >=radius:
            py = 0
    else:
        if px < 0:
            px = 0
        if px >= radius:
            px = radius-1
        if py < 0:
            py = 0
        if py >= radius:
            py = radius - 1
            


            
            
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
(location,cmds)=where(px,py)
prt("Current location: "+location,REPL)

while True:
  
  
    prt("Next action? "+cmds+"?",REPL)
    dir = intpt(cmds,REPL)
    compthink()
    
    chgloc(dir)
    (location,cmds)=where(px,py)
    
    prt("Current location: "+location,REPL)


