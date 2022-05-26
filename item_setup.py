import text
import textwrap
from options import width, developer_mode, game_running, player_location  

########## ITEM SETUP ##########

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

    def desc(self): #return correct description depending on if it is moved for look command
        if self.has_moved == True:
            return self.moved_description
        else:
            return self.description
            
    def exam(self): #examine
        if self.has_moved == True:
            return self.examine_description_moved
        else:
            return self.examine_description

    def special_function(self, action): #special unique function
        special_items_list = [book]
        if self not in special_items_list:
            return False
        if self == book: #the book pull action moves the bookshelf
            if action == "pull":
                print(textwrap.fill(text.book_pull, width))
                bookshelf.has_moved = True
                book.has_moved = True
    
class Container(Object): #container class
    def __init__(self, description, moved_description, examine_description, examine_description_moved, move, take, pull, can_move, can_take, can_pull, name, contents, open, can_open, see_contents):
        super().__init__(description, moved_description, examine_description, examine_description_moved, move, take, pull, can_move, can_take, can_pull, name)
        self.contents = contents
        for i in self.contents:
            i.in_container = self
        self.open = open
        self.can_open = can_open
        self.see_contents = see_contents
                
    def contains(self, examine = False): #print out contents
        if self.see_contents == False and examine == False: #return if you can't see the contents
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

class Literature(Object):
    def __init__(self, description, moved_description, examine_description, examine_description_moved, move, take, pull, can_move, can_take, can_pull, name, type, pg_num, current_pg, open, can_open, pages):
        super().__init__(description, moved_description, examine_description, examine_description_moved, move, take, pull, can_move, can_take, can_pull, name)

        self.type = type
        self.pg_num = pg_num
        self.current_pg = current_pg
        self.open = open
        self.can_open = can_open
        self.pages = pages

    def exam(self):
        if self.has_moved == True:
            x = self.examine_description_moved
        else:
            x = self.examine_description

        if self.can_open == True:
            if self.open == True:
                x += " (which is open)"
            else:
                x += " (which is closed)"
        return x
            
#add items to classes
notebook = Literature(text.notebook_look, text.notebook_moved, text.notebook_examine, text.notebook_examine_moved, text.notebook_move, text.notebook_take, "", can_move = True, can_take = True, can_pull = False, name = "notebook", type = "book", pg_num = 3, current_pg = 0, open = False, can_open = True, pages = text.notebook_pgs)

fountain_pen = Object(text.fountain_pen_look, text.fountain_pen_moved, text.fountain_pen_examine, text.fountain_pen_examine_moved, text. fountain_pen_move, text.fountain_pen_take, "", can_move = True, can_take = True, can_pull = False, name = "fountain pen")

inkwell = Object(text.inkwell_look, text.inkwell_moved, text.inkwell_examine, text.inkwell_examine_moved, text.inkwell_move, text.inkwell_take, "", can_move = True, can_take = True, can_pull = False, name = "inkwell")

bookshelf = Object(text.bookshelf_look, text.bookshelf_moved, text.bookshelf_examine, text.bookshelf_examine_moved, text.bookshelf_move, text.bookshelf_take, text.bookshelf_pull, can_move = False, can_take = False, can_pull = True, name = "bookshelf")

lamp = Light(text.lamp_look, text.lamp_moved, text.lamp_examine, text.lamp_examine_moved, text.lamp_move, text.lamp_take, "", can_move = True, can_take = False, can_pull = False, name = "lamp", current_status = True, on_level = 5)

# CONTAINERS #
table = Container(text.table_look, text.table_moved, text.table_examine, text.table_examine_moved, text.table_move, text.table_take, "", can_move = False, can_take = False, can_pull = False, name = "table", contents = [notebook, fountain_pen, inkwell, lamp], open = True, can_open = False, see_contents = True)
# \CONTAINERS #

chair = Object(text.chair_look, text.chair_moved, text.chair_examine, text.chair_examine_moved, text.chair_move, text.chair_take, "", can_move = True, can_take = False, can_pull = False, name = "chair")

piano = Piano(text.piano_look, text.piano_moved, text.piano_examine, text.piano_examine_moved, text.piano_move, text.piano_take, "", can_move = False, can_take = False, can_pull = False, name = "piano")

lantern = Light(text.lantern_look, text.lantern_moved, text.lantern_examine, text.lantern_examine_moved, text.lantern_move, text.lantern_take, "", can_move = True, can_take = True, can_pull = False, name = "lantern", current_status = False, on_level = 2)

book = Object("", "", text.book_examine, text.book_examine_moved, text.book_move, text.book_take, "", can_move = False, can_take = False, can_pull = True, name = "book")

grate = Object(text.grate_look, text.grate_moved, text.grate_examine, text.grate_examine_moved, text.grate_move, text.grate_take, text.grate_pull, can_move = False, can_take = True, can_pull = True, name = "grate")