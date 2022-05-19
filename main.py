"""
Hello! This is the program I made for my final assignment. It is a text based RPG similar to zork.
I have never made anything even close to this big in python, but maybe in other languages such as 
html (which I am not that great at, but managed to make my own personal website which barely works.)
I highly encourage you to try playing the game rather than looking through the code first! This 
took me a long time to make and I am happy with how it has ended up. There are a lot of things which 
I would like to add but could not do with the time given and my current knowlege. For a list of variables 
and more info on how this program works, please visit the README.md file. (if I get that done lol)

Enjoy!!!
-Justin
"""
import text #import stuff
import textwrap
import time
import classes########## OPTIONS: ##########
screen_size = 40
width = screen_size
developer_mode = False #turn on for debug settings: skips the menu and adds extra commands

if developer_mode == True:
    game_running = True
    player_location = [1,1]
else:
    game_running = False
    player_location = ["menu"]

z = 1 #set player z coordinate

########## ITEM SETUP ##########
inventory = [] #setup player inventory

class Object:
    has_moved = False
    in_container = None
    been_pulled = False
    special_function = False
    def __init__(self, description, moved_description, examine_description, examine_description_moved, move, take, pull, can_move, can_take, can_pull, name):
        self.description = description
        self.moved_description = moved_description
        self.examine_description = examine_description
        self.examine_description_moved = examine_description_moved
        self.move = move
        self.take = take
        self.pull = pull
        self.can_move = can_move
        self.can_take = can_take
        self.can_pull = can_pull
        self.name = name

    def desc(self): #return correct description depending on if it is moved
        if self.has_moved == True:
            return self.moved_description
        else:
            return self.description
            
    def exam(self):
        if self.has_moved == True:
            return self.examine_description_moved
        else:
            return self.examine_description

    def special_function(self, action):
        special_items_list = [book]
        if self not in special_items_list:
            return False
        if self == book: #the book pull action moves the bookshelf
            if action == "pull":
                print(textwrap.fill(text.book_pull, width))
                bookshelf.has_moved = True
    
class Container(Object):
    def __init__(self, description, moved_description, examine_description, examine_description_moved, move, take, pull, can_move, can_take, can_pull, name, contents, open, can_open, see_contents):
        super().__init__(description, moved_description, examine_description, examine_description_moved, move, take, pull, can_move, can_take, can_pull, name)
        self.contents = contents
        for i in self.contents:
            i.in_container = self
        self.open = open
        self.can_open = can_open
        self.see_contents = see_contents
                
    def contains(self, examine = False): #print out contents
        if self.see_contents == False and examine == False: #return if you cant see the contents
            return self.description[0] + ". "
        elif len(self.contents) == 0:
            return self.description[0] + ". "
        elif self.open == False:
            return self.description[0] + " which is closed. "
        else:
            x = []
            for i in self.contents:
                x.append(i.description)
            if len(x) > 1:
                y = '{} and {}'.format(', '.join(x[:-1]), x[-1])
            else:
                y = x[0]
            if examine == True: #return without "north of you is ... if examining" 
                return self.description[1].format(" " + y) + ". "
            else:    
                return self.description[0] + self.description[1].format(" " + y) + ". "

class Light(Object):
    def __init__(self, description, moved_description, examine_description, examine_description_moved, move, take, pull, can_move, can_take, can_pull, name, current_status, on_level):
        super().__init__(description, moved_description, examine_description, examine_description_moved, move, take, pull, can_move, can_take, can_pull, name)
        self.current_status = current_status
        self.on_level = on_level

class Piano(Object):
    been_played = False
    def __init__(self, description, moved_description, examine_description, examine_description_moved, move, take, pull, can_move, can_take, can_pull, name):
        super().__init__(description, moved_description, examine_description, examine_description_moved, move, take, pull, can_move, can_take, can_pull, name)

    def played(self, status = None): #piano logic
        if status == True or status == False:
            self.been_played = status
    
        if self.been_played == False:
            bookshelf.examine_description = text.bookshelf_examine
            self.examine = text.piano_examine

        elif self.been_played == True:
            bookshelf.examine_description = text.bookshelf_examine_piano_played
            self.examine = text.piano_examine_played
            
        return self.been_played

    def exam(self):
        return self.examine

class Literature(Object):
    def __init__(self, description, moved_description, examine_description, examine_description_moved, move, take, pull, can_move, can_take, can_pull, name, type, pg_num, current_pg, open, can_open, pages):
        super().__init__(description, moved_description, examine_description, examine_description_moved, move, take, pull, can_move, can_take, can_pull, name)

        self.type = type
        self.pg_num = pg_num
        self.current_pg = current_pg
        self.open = open
        self.can_open = can_open
        self.pages = pages
    
    def read(self): #book/paper reading
        if self.type == "book":
            if self.open == True:
                return self.pages[self.current_pg]
            else:
                return "The book is closed! Use [open book] to open it."
        elif self.type == "page":
            return self.pages[0]

#add items to classes
notebook = Literature(text.notebook_look, text.notebook_moved, text.notebook_examine, text.notebook_examine_moved, text.notebook_move, text.notebook_take, "", can_move = True, can_take = True, can_pull = False, name = "notebook", type = "book", pg_num = 3, current_pg = 0, open = False, can_open = True, pages = text.book_pgs)

fountain_pen = Object(text.fountain_pen_look, text.fountain_pen_moved, text.fountain_pen_examine, text.fountain_pen_examine_moved, text. fountain_pen_take, "", text.fountain_pen_move, can_move = True, can_take = True, can_pull = False, name = "fountain pen")

inkwell = Object(text.inkwell_look, text.inkwell_moved, text.inkwell_examine, text.inkwell_examine_moved, text.inkwell_move, text.inkwell_take, "", can_move = True, can_take = True, can_pull = False, name = "inkwell")

bookshelf = Object(text.bookshelf_look, text.bookshelf_moved, text.bookshelf_examine, text.bookshelf_examine_moved, text.bookshelf_move, text.bookshelf_take, text.bookshelf_pull, can_move = False, can_take = False, can_pull = True, name = "bookshelf")

lamp = Light(text.lamp_look, text.lamp_moved, text.lamp_examine, text.lamp_examine_moved, text.lamp_move, text.lamp_take, "", can_move = True, can_take = False, can_pull = False, name = "lamp", current_status = True, on_level = 5)

note = Object(text.note_look, text.note_moved, text.note_examine, text.note_examine_moved, text.note_move, text.note_take, text.note_pull, can_move = True, can_take = True, can_pull = True, name = "note") #need to put container contents BEFORE container

# CONTAINERS #
table = Container(text.table_look, text.table_moved, text.table_examine, text.table_examine_moved, text.table_move, text.table_take, "", can_move = False, can_take = False, can_pull = False, name = "table", contents = [notebook, fountain_pen, inkwell, lamp], open = True, can_open = False, see_contents = True)
# \CONTAINERS #

chair = Object(text.chair_look, text.chair_moved, text.chair_examine, text.chair_examine_moved, text.chair_move, text.chair_take, "", can_move = True, can_take = False, can_pull = False, name = "chair")

piano = Piano(text.piano_look, text.piano_moved, text.piano_examine, text.piano_examine_moved, text.piano_move, text.piano_take, "", can_move = False, can_take = False, can_pull = False, name = "piano")

lantern = Light(text.lantern_look, text.lantern_moved, text.lantern_examine, text.lantern_examine_moved, text.lantern_move, text.lantern_take, "", can_move = True, can_take = True, can_pull = False, name = "lantern", current_status = False, on_level = 2)

book = Object("", "", "", "", text.book_move, text.book_take, "", can_move = False, can_take = False, can_pull = True, name = "book")

grate = Object(text.grate_look, text.grate_moved, text.grate_examine, text.grate_examine_moved, text.grate_move, text.grate_take, text.grate_pull, can_move = False, can_take = True, can_pull = True, name = "grate")

########## SETUP ITEM LOCATION DEFAULTS ##########
objects_room1 = [bookshelf, table, notebook, fountain_pen, inkwell, chair, piano, lantern, lamp, book]
objects_staircase = []
objects_concrete_room = [grate]

def update_objs(): 
    global objects_room1, objects_staircase, objects_conctete_room, objects_currentloc
    piano.played()
    
    cross_reference_items = {
        "menu,1": objects_room1, 
        "1,1,1": objects_room1,
        "2,1,1": objects_room1,
        "3,1,1": objects_staircase,
        "1,1,0": objects_concrete_room,
        "2,1,0": objects_concrete_room,
        "3,1,0": objects_concrete_room,
        "4,1,0": objects_concrete_room,
        "5,1,0": objects_concrete_room,
        "6,1,0": objects_concrete_room,
        "7,1,0": objects_concrete_room,
    }
    
    try:
        objects_currentloc = cross_reference_items[",".join(str(i) for i in player_location) + "," + str(z)]
    except KeyError:
        objects_currentloc = []
        
update_objs() #call the function to set up all the items

class Location:
    def __init__(self, m_north, m_south, m_east, m_west, l_north, l_south, l_east, l_west, t_north, t_south, t_east, t_west, light, look, title, print_look = False):
        self.m_north = m_north #if moving is possible
        self.m_south = m_south
        self.m_east = m_east
        self.m_west = m_west
        self.l_north = l_north #location if moving
        self.l_south = l_south
        self.l_east = l_east
        self.l_west = l_west        
        self.t_north = t_north #text to orint when moving
        self.t_south = t_south
        self.t_east = t_east
        self.t_west = t_west
        self.light = light
        self.look = look
        self.title = title
        self.print_look = print_look
########## INITIALIZE MAP ##########
def updatemap():
    global locations

    locations = {
    "1,1,1":Location(False, False, bookshelf.has_moved, False, [], [], [3,1,1], [], "", "", "", "", 0, text.main_room_look, "Main Room"),
    "3,1,1":Location(False, False, False, False, [], [], [], [], "", "", "", "", 0, text.staircase_look, "Staircase"),
    "3,1,0":Location(False, grate.been_pulled, False, False, [], [3,4,0], [], [], "", "You crawl through the grate", "", "", 6, text.concrete_room_look, "Concrete Chamber"), 
    "3,4,0":Location(grate.been_pulled, True, True, False, [3,1,0], [6,7,0], [8,4,0], [], "", "", "", "", 10, text.look_3_4_0, "North Of Stream", print_look = True),
    "8,4,0":Location(False, True, True, True, [], [9,8,0], [13,2,0], [3,4,0], "", "", "", "", 10, text.look_8_4_0, "North Of Stream", print_look = True),
    "13,2,0":Location(False, True, True, True, [], [6,7,0], [6,7,0], [8,4,0], "", "", "", "", 10, text.look_13_2_0, "On Tree Trunk", print_look = True),
    "9,8,0":Location(False, False, False, False, [8,4,0], [10,12,0], [6,7,0], [6,7,0], "", "", "", "", 10, text.look_9_8_0, "South Of Stream", print_look = True),
    "6,7,0":Location(False, False, False, False, [], [], [], [], "", "", "", "", 10, "", "Inside Stream", print_look = True),
    "10,12,0":Location(False, False, False, False, [], [], [], [], "", "", "", "", 10, "", "Forest", print_look = True),
    }

updatemap()

########## DEFINE ACTIONS AND OTHER FUNCTIONS ##########
def locstr(): #this was repeated a lot so I made a function
    return ",".join(str(i) for i in player_location) + "," + str(z) 
def lightlevel(): #return light level of current location
    total_light = 0
    total_light += locations[locstr()].light
    for i in objects_currentloc + inventory:
        if isinstance(i, Light):
            if i.current_status == True:
                total_light += i.on_level
    return total_light
def game_end(cause):
    global game_running
    deathcauses = {"piano":text.piano_death, "stream":text.stream_death}
    print(textwrap.fill(deathcauses[cause], width))
    print(text.game_over)
    exit()

trig_hall = False #causes it to only print once
def trigger(cause): #trigger code if player is in certain place
    global trig_hall, z
    if cause == "3,1,1" and trig_hall == False:
        bookshelf.has_moved = False
        print(locations[locstr()].title+":\n")
        if lightlevel() == 0:        
            print(textwrap.fill(text.bookshelf_close[0], width))
        else:
            print(textwrap.fill(text.bookshelf_close[1], width))
        trig_hall = True
        z = 0
        return
    elif cause == "6,7,0":
        game_end("stream")
    elif cause == "10,12,0":
        end()

def help():
    for i in text.helplist:
        print(textwrap.fill(i, width))
def printinv(): #print inventory contents
    if len(inventory) == 0:
        print(textwrap.fill("Your inventory is currently empty! To pick things up, use the [take] command.", width))
    else:
        print("You currently have:")
        for i in inventory:
            print("    - "+i.name)

def quit(): #quit game dialogue
    print("Are you sure? (y/n)")
    while True:
        action = input("> ").lower()
        
        if action == "y":
            print("Shame, hope to see you again!")
            exit()
        elif action == "n":
            print("Returning...")
            return
        else:
            print("Sorry, you can't do that!")

def look(): #prints current surroundings
    if lightlevel() <= 0:
        print(textwrap.fill("you are unable to see anything in the dark!", width))
        return
    x = ""
    x += locations[locstr()].look + " "
    for i in objects_currentloc:
        if i.in_container != None or i in inventory:
            continue
        if isinstance(i, Container):
            x = x + i.contains()
        else:
            x = x + (i.desc())
    print(locations[locstr()].title+":\n")
    print(textwrap.fill(x, width))

def examine(item): #gies detailed description of item
    if lightlevel() <= 0:
        print(textwrap.fill("you are unable to see anything in the dark!", width))
        return
    for i in objects_currentloc + inventory:
        if i.name == item:
            if isinstance(i, Container):
                print(textwrap.fill(i.exam(), width))
            return
    print("That item does not exist!")
    return

def move(item): #move an item
    if lightlevel() <= 0:
        print(textwrap.fill("you are unable to see anything in the dark!", width))
        return
    for i in objects_currentloc:
        if i.name == item:
            if i.has_moved == True:
                print(textwrap.fill("You already moved this and I could not be bothered currently to allow you to move it back.", width))
                return

            if i.can_move == True:
                print(textwrap.fill(i.move, width))
                i.has_moved = True
                return
            else:
                print(textwrap.fill(i.move, width))
                return
    print("That item does not exist!")

def play(arg): #play an item
    global piano, bookshelf
    if lightlevel() <= 0:
        print(textwrap.fill("you are unable to see anything in the dark!", width))
        return
        arg = arg.replace(" ", "")

    if piano.played == True:
        print("You already played it!")
        return
        
    if arg == "adbg":
        piano.played(True)
        print(textwrap.fill(text.piano_notes_correct, width))

    else:
        print(textwrap.fill(text.piano_notes_incorrect_first, width) + "\n")
        time.sleep(3)
        print(textwrap.fill(text.piano_notes_incorrect_second, width) + "\n")
        time.sleep(3)
        print(textwrap.fill(text.piano_notes_incorrect_third, width) + "\n")
        time.sleep(3)
        if width >= 40:
            print(text.piano_notes_incorrect_art)
        game_end("piano")
        

def pull(item): #pull an item
    if lightlevel() <= 0:
        print(textwrap.fill("you are unable to see anything in the dark!", width))
        return
    for i in objects_currentloc:
        if i.name == item:
            if i.been_pulled == True:
                print("You already pulled this!")
                return
            if i.can_pull == False:
                print("You can't pull this!")
                return    

            i.been_pulled = True
            if i.special_function("pull") != False:
                i.special_function("pull")
            else:
                print(textwrap.fill(i.pull, width))
            return
    print(textwrap.fill("You look around and do not see that item anywhere.", width))
            
def navigation(direction): #move around n s w or w
    global player_location, z
    x = locstr()
    if direction in ["north", "n"]:
        if locations[x].m_north == True:
            if len(locations[x].t_north) > 0:
                print(locations[x].t_north)
            else:
                print("Going north")
            print("")

            player_location = (locations[x].l_north)[:-1]
            z = (locations[x].l_north)[-1]
        else:
            print("You cant go there!")
            
    if direction in ["south", "s"]:
        if locations[x].m_south == True:
            if len(locations[x].t_south) > 0:
                print(locations[x].t_south)
            else:
                print("Going south")
            print("")
            
            player_location = (locations[x].l_south)[:-1]
            z = (locations[x].l_south)[-1]
        else:
            print("You cant go there!")
            
    if direction in ["east", "e"]:
        if locations[x].m_east == True:
            if len(locations[x].t_east) > 0:
                print(locations[x].t_east)
            else:
                print("Going east")
            print("")
                
            player_location = (locations[x].l_east)[:-1]
            z = (locations[x].l_east)[-1]
        else:
            print("You cant go there!")
            
    if direction in ["west", "w"]:
        if locations[locstr()].m_west == True:
            if len(locations[x].t_west) > 0:
                print(locations[x].t_west)
            else:
                print("Going west")
            print("")
            
            player_location = (locations[x].l_west)[:-1]
            z = (locations[x].l_west)[-1]
        else:
            print("You cant go there!")
    updatemap()
    
def take(item):  #take an item and put it in inventory
    if lightlevel() <= 0:
        print(textwrap.fill("you are unable to see anything in the dark!", width))
        return
    for i in objects_currentloc:
        if i.name == item:
            if i.can_take == True:
                if i.in_container != None:
                    (i.in_container).contents.remove(i)
                    i.in_container = None
                objects_currentloc.remove(i)
                inventory.append(i)
                print(textwrap.fill(i.take, width))
                return
            else:
                print(textwrap.fill(i.take, width))
                return
    for i in inventory:
        if i.name == item:
            print("You are already holding that!")
            return
    print("That item does not exist!")
    
def put(item, location): #put item from inventory in container
    if lightlevel() <= 0:
        print(textwrap.fill("you are unable to see anything in the dark!", width))
        return
    for i in inventory:
        if i.name == item:
            for x in objects_currentloc:
                if isinstance(x, Container) and x.name == location:
                    objects_currentloc.append(i)
                    x.contents.append(i)
                    i.in_container = x
                    inventory.remove(i)
                    return
    print("You do not have that item!")
    return  
def activate(action, item): #activate item such as light and turn it on/off
    statdict = {"on":True, "off":False}
    if action not in statdict.keys():
        print("Turn it on or off?")
        return
    status = statdict[action]
    for i in inventory + objects_currentloc:
        if i.name == item:
            if isinstance(i, Light):
                if i.current_status != status:
                    i.current_status = status
                    print("You turn the {} {}".format(item, action))
                    return
                else:
                    print("The {} is already {}!".format(item, action))
                    return
            else:
                print("You  can't turn {} the {}!".format(action, item))
                return
    print(textwrap.fill("You do not have that item anywhere near you.", width))


########## MAIN ##########
def open(item, action):
    for i in objects_currentloc + inventory:
        if i.name == item:
            if isinstance(i, Container) or isinstance(i, Literature):
                if i.can_open == True:
                    if i.open == False and action == "open":
                        i.open = True
                        i.current_pg = 1
                        print("You open the {}".format(item))
    
                    elif i.open == True and action == "close":
                        i.open = False
                        print("You close the {}".format(item))
                    return
            else:
                print("You can't open that!")
                return
    print("You can't do that!")


def read(item):
    for i in objects_currentloc + inventory:
        if isinstance(i, Literature):
            if i.name == item:
                if i.open == True:
                    while i.open == True:
                        print(textwrap.fill(i.pages[i.current_pg], width))
                        print("\npage: " + str(i.current_pg))
                        print("\n[n] for next page\n[p] for previous page")
                        print(textwrap.fill("[close] to stop reading and close the book", width))
                        action = input("\n> ").lower() #player input
                        if action == "n":
                            if i.current_pg + 1 <= i.pg_num:
                                i.current_pg += 1
                            else:
                                print("You are on the last page!\n")
                        elif action == "p":
                            if i.current_pg - 1 <= i.pg_num:
                                i.current_pg -= 1
                            else:
                                print("You are on the first page!\n")                    
                        elif action == "close":
                            i.open = False
            print("The book is closed! use [open] to open it!")

def end():
    print("You have escaped!")
    print(textwrap.fill("I do not have enough time to go any further. I hope you enjoyed my first proper Python program. I know it may not be the most complicated or even hard to beat game made with python, but I am happy with how it came out. If I could change stuff, I would make it more challenging with a better story, and also try to use classes more. I would like to add some way of fighting and health scores. I may do this on my own time in the future, but for now this is all I have.", width))
    print("- Justin")
        
while player_location == ["menu"]:
    home_restart = False
    print(text.logo)
    print("")
    print(text.intro)
    commands = ["help", "start", "quit",]
    
    while game_running == False and home_restart == False:
        action = input("\n> ").lower()
    
        if action not in commands:
            print("Sorry, you can't do that!")
            continue
    
        if action == "help":
            help()
            
        if action == "quit":
            quit()
            home_restart = True
            
        if action == "start":
            game_running = True
            player_location = [1,1]

            
#setup for the main loop:
look()

commands = ("north", "south", "east", "west", "n", "s", "e", "w", "help", "inventory", "i", "quit", "look", "l", "examine", "move", "play", "pull", "take", "put", "turn", "open", "close", "read")
movements = ("north", "south", "east", "west", "n", "s", "e", "w")

# main loop:
while game_running == True:
    trigger(locstr()) #check if in special location, if so run code
    update_objs() #update the objects
    if developer_mode == True:
        print(locstr())
        print(lightlevel())
    updatemap() #update the map 
    if locations[locstr()].print_look == True:
        look()
    action = input("\n> ").lower().split() #player input
    
    # single argument commands
    if len(action) <= 0:
        print("Please input something!")
        continue

    if action[0] == "compass":
        print(text.compass)
        continue
    
    elif action[0] not in commands:
        print("Sorry, you can't do that!")
        continue

    elif action[0] in ["look", "l"]: 
        look()
        continue
    
    elif action[0] == "quit": 
        quit()
        continue
    
    elif action[0] == "help": 
        help()
        continue

    elif action[0] in ["inventory", "i"]:
        printinv()
        continue
    
    elif action[0] in movements:
        navigation(action[0])
        continue
    
    # multi argument commands
    arg = " ".join(action[1:])
    if action[0] == "examine": 
        examine(arg)
        
    elif action[0] == "move":  
        move(arg)
        
    elif action[0] == "pull": 
        pull(arg)
        
    elif action[0] == "play":  
        if player_location == [1,1]:
            play(arg)
        else:
            print(textwrap.fill("You look around and remember that there is nothing near you that you can play.", width))

    elif len(arg) <= 1:
    	print("Missing argument!")
    	continue
		
    elif action[0] == "take": 
        take(arg)

    elif action[0] == "put": 
        command = action[0]
        if "in" in action:
            x = action.index("in")
        elif "on" in action:
            x = action.index("on")
        else:
            print("Where would you like to put the item?")
            continue
        item = " ".join(action[1:x])
        container = " ".join(action[x+1:])
        put(item, container)
        print("You put the " + item + " " + action[x] + " the " + container)
        
    elif action[0] == "turn":
        activate(action[1], action[2])
        if lightlevel() <= 0:
            pass

    elif action[0] in ["open", "close"]:
        open(arg, action[0])

    elif action[0] == "read":
        read(arg)