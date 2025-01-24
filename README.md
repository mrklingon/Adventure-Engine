# Adventure-Engine
NeoTrinkey code for simple adventure gaming

* intput.py - pass a string "choices" to intpt(choices) and return one of the letters to calling routine. eg intpt("nsew") and you'll get back n,s,e,or w. This can be navigation.
* wise.py - choose a line from a text file. This file will be a linear list of an AxA array. Program will be used for description of current location
* advent.py - (code.py when running). Tracks user location in AxA array, calls wise.py to find and print location, then offers chance to move to N,S,E,W direction and retrieves choice from intpt(), calculates new location and prints it.
* prt.py - allows printing to REPL or via HID as typed output.
* ship.adv - sample map for a 3x3 ship
* magic.adv - sample map for a 5x5 magical realm. WRAP should be set to True, and radius to 5.

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

When running, you are given "Current location:" and then offered the directions you can go. Touching pad #1 toggles between choices, touching pad #2 chooses the current one.  
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
<hr>
# Magic Adventure Map

Here's another map, that is defined in the repository file "magic.adv"   

![image](https://github.com/user-attachments/assets/601c501b-368a-430c-a3b1-4908c6cbea0a)

To use this map, change map= to **map="magic.adv"**, **radius=5** and **WRAP=True**  
Turning on WRAP means from some rooms you can go from one edge of the map to the far side. The gaps in the map indicate the directions from each cell that are available.   
**note** The "tower" room can be exited going 'south'... but NOT entered from the south going north.

Here's a sample run:  
```
Current location: Forest south of dungeon
Next action? ew
?
e!
Current location: Road to castle

Next action? nsew?
n!
s!
Current location: Bridge over river
Next action? ns
?
n!
s!
Current location: Road to castle

Next action? nsew?
n!
s!
e!
w!
Current location: Forest bank

Next action? nsew?
n!
s!
Current location: Wilds
Next action? nwe
?
n!
w!
e!
Current location: Road to castle
Next action? wne
?
w!
n!
e!
Current location: Wizard's Garden
Next action? wne
?
w!
n!
e!
Current location: Wizard's hut

Next action? nsew?
n!
s!
Current location: Forest

Next action? nsew?
n!
s!
e!
w!
Current location: Castle tower looming over kingdom
Next action? wse
?
w!
Current location: Castle
Next action? ews
```

At present the Adventure Engine lets you define and navigate a mapped space. Next steps involve adding appropriate command codes for game-actions and a dispatcher to handle none-movement choices.
