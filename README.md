# SilentKey
## My first python program (kinda)
For a while now I have been trying to learn programming, but never really got around to it. I always ended up trying and then giving up shortly later. It was only when the programming unit in school came around that I decided to take it seriously. For my unit project, I decided that I wanted to do something that would help me learn about more advanced methods such as object-oriented programming (and also markdown!). 

I figured I would do something that I had been interested in for a while: **A text based game.** Half way through making it I was tapping on my desk and accidentally tapped "SK" in morse code, which means "Silent Key". It is used when a morse radio operator passes away, to signal that their key will be "silent" (no longer transmitting). Before this the only name I had for the game was terrible, so I figured I would use SilentKey instead.

## How to run the program:
#### With IDE:
Copy at minumum the four main files: `main.py`, `item_setup.py`, `text.py`, and `options.py` into a python IDE set to python version 3 and run the `main.py` file. The program uses two inbuilt packages: `textwrap` and `time`

## File organisation:
The program is split into multiple different files which serve different purposes:

- `main.py` does the bulk of the work, including user input and commands
- `item_setup.py` sets up all the items in the game, which all get assigned to a class depending on what they are
- `text.py` holds all text for the program. This takes up a lot of space so I put it in a seperate file.
- `options.py` holds some basic options such as a screen size variable and a debug mode

## How it works:
The program asks the user for a command and then cycles through, checking if it matches with anything. If it finds a match, it runs the code for that command. If not, it prints out an error. Some actions have functions, and others don't. That's because some things need to be run elsewhere and it just made more sense to make a function.

### Functions:
#### Basic functions:
|Function:                |Description:                                                                           |
|-------------------------|---------------------------------------------------------------------------------------|
|`update_objs()          `|Updates objects and sets up the `objects_currentloc` list                              |
|`updatemap()            `|Updates the map locations because variables only get defined once                      |
|`locstr()               `|Returns the current coordinates in string form, used in other functions                |
|`lightlevel()           `|Returns light level of the current location                                            |
|`game_end(cause)        `|Ends the game and prints message depending on `cause`                                  |
|`trigger(cause)         `|Used to trigger things when player is at a cartain location                            |
|`helptxt()              `|Prints out the commands                                                                |
|`printinv()             `|Prints inventory contents                                                              |
|`quit()                 `|Quits the game                                                                         |
|`look()                 `|Prints surrounding objects                                                             |
|`examine(item)          `|Gives closer look at item                                                              |
|`move(item)             `|Moves item (This did not really get used and is too vague. More trouble than good!)    |
|`play(arg)              `|Plays an instrument (the piano!)                                                       |
|`pull(item)             `|Pulls on object                                                                        |
|`navigation(direction)  `|Accepts the nsew commands and moves player                                             |
|`take(item)             `|Adds item to players inventory and removes it from environment                         |
|`put(item, location)    `|Adds item to container (DOES NOT CHECK IF CONTAINER IS OPEN! BUG)                      |
|`activate(action, item) `|Turns on an item (like a light!)                                                       |
|`openclose(item, action)`|Opens or closes container                                                              |
|`read(item)             `|Opens the read dialogue for literature                                                 |
|`end()                  `|Prints the end of the game (credits?)                                                  |
#### Functions in classes:
Next section!

### Classes:

**`Object` | Base level class with three functions:**
- `desc()` | Returns the current description of the item. Used for look command
- `exam()` | Returns the current examine description of the item. Used for examine command
- `special_function(action)` | Runs special code depending on item (I do not like how I did this!)

**Default Variables:**
- has_moved = False
- in_container = None
- been_pulled = False

**Arguments:**
- description
- moved description
- examine description
- examine description moved
- move
- take
- pull
- can move
- can take
- can pull
- name

---

**`Container` | Object that can hold other items inside. Has one unique function:**
- `contains(examine = False)` | Prints out contents of container 

**Arguments:**
- description
- moved description
- examine description
- examine description moved
- move
- take
- pull
- can move
- can take
- can pull
- name
- contents
- open
- can_open
- see_contents
  
---

**`Literature` | Item that can be read. Has one unique function:**
- `exam()` | Same as standard object, but also returns the state of the item if it's a book (closed or open)

**Arguments:**
- description
- moved description
- examine description
- examine description moved
- move
- take
- pull
- can move
- can take
- can pull
- name
- type
- pg_num
- current_pg
- open
- can_open
- pages

---

**`Piano` | Class for the piano:**
- `played(status = None)` | Piano logic that controls piano/bookshelf actions

**Arguments:**
- description
- moved description
- examine description
- examine description moved
- move
- take
- pull
- can move
- can take
- can pull
- name

---

**`Light` | Object that can emmit light. No unique functions.**

**Arguments:**
- description
- moved description
- examine description
- examine description moved
- move
- take
- pull
- can move
- can take
- can pull
- name
- current status
- on level
- has moved
- in container
- been played

---

**`Location` | Used when defining new locations**

**Arguments:**
- self
- m_north
- m_south
- m_east
- m_west
- l_north
- l_south
- l_east
- l_west
- t_north
- t_south
- t_east
- t_west
- light
- look
- title
- print_look = False

Arguments that start with:
- m - Boolean, tells program if you can move in direction from the location
- l - The location to move to depending on the direction
- t - Text to print when moving

---

### Commands: 

| Command(s)              | Description                    | 
|-------------------------|--------------------------------|
|help                     | Print help menu                |
|quit                     | Quit game                      |
|north, n                 | Go north                       |
|south, s                 | Go south                       |
|east, e                  | Go east                        |
|west, w                  | Go west                        |
|inventory, i             | Print inventory contents       |
|take [item]              | Take item (put it in inventory)|
|put [item] [in/on] [item]| Put item on/in table/container |
|look, l                  | Look around                    | 
|examine [item]           | Examine item                   |
|move [item]              | Move item                      |
|pull [item]              | Pull item                      |
|turn [on/off] [item]     | Turn on or off item            |
|open [item]              | Open item                      |
|close [item]             | Close item                     |
|read [item]              | Read piece of literature       |

## Next time:
I do plan on doing this again some time, and when I do there are lots of things I would change. I would plan things out better and organise things nicer. I would also make EVERYTHING an object in a class, so for example, you could examine the river or the log. I could even make rooms and the player a sub class of the container class. I would also add different endings and paths, rather than restricting the player to one trail. I may add in food, hunger and health along with fighting.