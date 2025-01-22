# Adventure-Engine
NeoTrinkey code for simple adventure gaming

* intput.py - pass a string "choices" to intpt(choices) and return one of the letters to calling routine. eg intpt("nsew") and you'll get back n,s,e,or w. This can be navigation.
* wise.py - choose a line from a text file. This file will be a linear list of an AxA array. Program will be used for description of current location
* advent.py - (code.py when running). Tracks user location in AxA array, calls wise.py to find and print location, then offers chance to move to N,S,E,W direction and retrieves choice from intpt(), calculates new location and prints it.
* prt.py - allows printing to REPL or via HID as typed output.
* ship.adv - sample map for a 3x3 ship

Code is a framework for having the NeoTrinkey navigate a space - dungeon, forest, spaceship. 

Set map=[file name] of list of room descriptions  
set radius=X where X is the size of the matrix. 3x3 or 5x5 for example  
set px and py to starting room.   eg. for a 3x3 map px=1 py=1 will set the start in the center of the map  
set WRAP = True for the map being a torus, and False for the map having edges you can't go beyond.  
sample map "ship.adv" defines a 3x3 map:  

```
communications bay|e
cockpit|wse
computer and navigation bay|w
sleeping quarters|e
wardroom
galley|w
storage|e
engines|new
power resources|w
```

**Note** some lines end with a "|" plus directions that can be followed from the room. If the room ends with "|e" for example, you can only leave to the East. If the line ends with no |+direction(s) the default is you can leave NSEW. (for example, the wardroom in this case).

The map below shows the rooms for ship.adv, and the gaps in the walls show which directions you can go. Only the wardroom allows passage in all four directions, NSEW.

![image](https://github.com/user-attachments/assets/8e362919-8d09-4e41-b0dc-c9bd03c3a1b2)

When running, you are given "Current location:" and the offered the directions you can go. Touching pad #1 toggles between choices, touching pad #2 chooses the current one.  
For example:   
```
Current location: wardroom

Next action? nsew?
n!
Current location: cockpit
Next action? wse
?
w!
s!
Current location: wardroom

Next action? nsew?
n!
s!
Current location: engines
Next action? new
?
n!
e!
Current location: power resources
Next action? w
?
w!
```

