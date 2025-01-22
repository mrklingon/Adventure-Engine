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
