"""
  _____ _ _           _   _  __          
 / ____(_) |         | | | |/ /          
| (___  _| | __ _ __ | |_| ' / __ _   _ 
 \___ \| | |/_ \ '_ \| __|  < /_ \ | | |
 ____) | | | __/ | | | |_| . \ __/ |_| |
|_____/|_|_|\__|_| |_|\__|_|\_\__|\__, |
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   __/ | 
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  |___/ 
  
_look: text to piece together when looking
_moved: text to piece together when looking if object has been moved
_examine: text for when item is examined
_examine_moved: text for when item is examined if object has been moved
_take: text for when taken, even if you can not take it
_move: text for when moving, even if you can not move it
"""
#################################################

main_room_look = "You are in main room" 
staircase_look = ""
concrete_room_look = "You are in a damp concrete room."
look_3_4_0 = "You’re standing on the bank of a stream, to your north you see a small opening in the side of a mound which you used to exit the concrete room. To your west there are some unstable looking rocks, which look extremely difficult to cross. You see a conveniently placed fallen tree trunk splayed across the stream which you could possibly balance across."
look_8_4_0 = "You’re standing on the bank of a ravenous stream. To your north lies a hill, likely containing the rooms in which you were trapped. You turn to your west and find a mound with an opening which you exited through from the concrete room. To your east is an elevated area where the hill leads to a dropoff which likely goes hundreds of feet down. You also see a conveniently placed fallen tree trunk splayed across the stream which you could possibly balance across."
look_13_2_0 = "You’re standing on the bank of a stream. To your east is a narrow path across, likely to send you to a watery grave. You turn to your west and meet a fallen oak tree, which you momentarily consider shimmying across to the other side. To your west you see a conveniently placed fallen tree trunk splayed across the stream which you could possibly balance across."
look_9_8_0 = "You’re balancing on the log over the rapids with your hands out to either side."

look_10_12_0 = ""

#################################################

bookshelf_look = "To your east is a bookshelf which reaches all the way up to the ceiling. "
bookshelf_moved = "To your east is a bookshelf reaching all the way up to the ceiling which has been slid to the left revealing a dark passage. "
bookshelf_examine = "You walk up to the bookshelf and take a good look at the plethora of literature before you. "

bookshelf_examine_moved = "You walk up to the bookshelf and take a good look at the plethora of literature before you. A dustless book has been pulled out and the bookshelf is slid over. "
bookshelf_take = "You bear hug the bookshelf and pull with all your might. It doesn’t budge."
bookshelf_move = "You push on the bookshelf from its side, it shouldn’t be nearly this heavy, so why is it?"
bookshelf_pull = "You pull hard on the bookshelf, but it won't budge. It must beattached to the wall."

book_pull = "You pull the dustless book out from the shelf by giving the top of the spine a tug. The book comes to a stop at a 40 degree angle and you hear the clicking of a complex mechanical system as the bookshelf slides to your left, revealing a dark passageway behind it. There is no way that you are going to see in there. "

book_move = "There is no room to move any of the books! "
book_take = "It seems that the books are glued to the bookshelf, why would this be?"
book_examine = "The books are lined incredibly neatly and all look similar. They are allquite dusty."
book_examine_moved = "A book has been pulled out, causing the bookshelf to slide. There is no dust on the spine."


bookshelf_close = {0:"You walk through the entrance and stare into the darkness. After taking a step forward there is a click from under your feet as one of the stones gets pressed in. You hear a rolling noise behind you as the passage gets pitch dark. You turn around quickly to find that the bookshelf has slid back. You are in complete darkness. You hear a man say \"I thought you would try to escape!\" behind you and then the floor folds down. You fall into a very damp chamber made out of concrete. The hatch clicks shut. You are locked in.", 
                   1:"You walk through the entrance and stare into the darkness. After taking a step forward there is a click from under your feet as one of the stones gets pressed in. You hear a rolling noise behind you as the passage darkens. You turn around quickly to find that the bookshelf has slid back. You hear footsteps behind you and when you look, you see a man in all black walking with purpose towards you. \"I thought you would try to escape!\" Before you can react he pulls a small lever on the wall and then the floor collapses below you. You fall into a very damp chamber made out of concrete. The hatch clicks shut. You are locked in." 
                  } #number indicates light level

#################################################

piano_look = "A large upright piano stands tall to your west. "
piano_moved = ""
piano_examine_moved = ""
piano_take = "You bend your legs and arch your back to lift up this humungous piano. You fail to lift even that side off the ground. This thing isn’t going anywhere."
piano_move = "You push on the piano with all your might, there’s no chance this hunk of an instrument is budging any time soon."

piano_notes_incorrect_first = "You hear a buzzer sound from behind the piano's siding that keeps getting louder. You feel surprisingly ashamed for some reason. "
piano_notes_incorrect_second = "You feel your ears aching with every passing second."
piano_notes_incorrect_third = "The piano explodes, sending you flying across the room. You no longer hear, or feel anything as you drop to the floor with shards of wood raining down on your corpse.\n"

piano_notes_incorrect_art = ""

piano_notes_correct = "You hear the melody you just played repeat and even become louder and more eloquent. A rather small fellow emerges from a small door in the piano you hadn’t noticed before, he points across the room to seemingly nothing important."

piano_examine = "You walk over to the piano, and the wooden siding on the front of the case has something engraved into it, you blow away the dust in order to see it better, and it has the numbers 1, 4, 2, 7 on it. You look down and see the keys have the remains of some painted letters on them, A through G in specific. [HINT: Use play followed by notes!]"
bookshelf_examine_piano_played = "You walk up to the bookshelf and take a good look at the plethora of literature before you. As you’re scanning over the books for possible clues, you spot a book with less dust on it than the others. "
piano_examine_played = "You see a small open door on the front of the piano with a small man with flaking paint pointing across the room to the bookshelf, but nothing that looks out of the ordinary"

piano_death = "You played music so bad even your instrument didn't like it. Nice one."

#################################################

table_look = ["North of you is a dusty old table", " with{} sitting on top"]
table_moved = ""
table_examine = "The table looks well used, and one of its legs is loose."
table_examine_moved = ""
table_take = "You can’t reach far enough around the table to be able to pick it up, and it’s unlikely that you could regardless."
table_move = "You take position on the side of the table, and you slide it along the old ruined wooden floorboards."

#################################################

notebook_look = "a notebook"
notebook_moved = "a notebook "
notebook_examine = "The notebook is old and tattered near the edges. The cover is blank."
notebook_examine_moved = "Would you look at that, the notebook is 3 inches from where you found it. The notebook is old and tattered near the edges. The cover is blank."
notebook_take = "You decide to take it along with you, after all, the writings of a man who went missing 3 years ago might fetch a high price on Gregslist."
notebook_move = "You slide the notebook to the right of where it previously was, although it’s difficult to determine why."
notebook_pgs = ["Day 1 - I’ve been learning more and more about this Kahmun fellow. He seems to be quite a prestigious figure within the culture. I’ll keep you posted as I find out more. - Cecil H. Thomas", "day 55 - i cant stop reading abut him hes all i think about i cant get him out he knows what im doing. ~Cecel h tomas", "Day 142 - he found me getoutgetoutgetoutgetoutgetoutgetoutgetoutgetoutgetoutgetoutgetoutgetoutgetoutgetoutgetoutgetoutgetoutgetout -IDONTKNOW", "page4"]

#################################################

fountain_pen_look = "a fountain pen"
fountain_pen_moved = "a fountain pen"
fountain_pen_examine = "The pen is of quite high quality, with gold plated linings near the tip. Part of you feels inadequate to hold something of this precious kind, but its beauty is somewhat degraded by the dust and mold settled upon the sleek curves. "
fountain_pen_examine_moved = "The pen looks slightly less satisfying when it’s not parallel to the notebook."
fountain_pen_take = "You put it in your back pocket, a pawn shop might give a kidney for something like this."
fountain_pen_move = "You move the pen over a bit from the notebook, without really knowing why anyone would do that."

#################################################

inkwell_look = "a stationary inkwell"
inkwell_moved = "a stationary inkwell"
inkwell_examine = "The inkwell is as essential to the use of the pen as the pen is itself, that is if it wasn't all dried up. You turn it over and see the brand \"Rupert Calligraphy\" scribed into the bottom."
inkwell_examine_moved = "The inkwell is a few inches over and as essential to the use of the pen as the pen is itself. Someone who uses Reddit might caption it “Name a more iconic duo”"
inkwell_take = "You decide to stuff this beautiful antique into your infinitely expanding text based game pockets which defy the rules of space and time as we know them."
inkwell_move = "You slide the inkwell over a few centimetres, but why?"

#################################################

lantern_look = "A gas lantern sits on the floor on your north-west. "
lantern_moved = "A gas lantern sits on the floor on your north-west. "
lantern_examine = "The lantern looks old, and similarly to everything else, is covered in dust. You give it a shake and hear a sloching sound of gas inside. "
lantern_examine_moved = "The lantern looks old, and similarly to everything else, is covered in dust. You give it a shake and hear a sloching sound of gas inside. "
lantern_take = "You pick up the lantern and carry it by the thin metal handle. This could be useful later."
lantern_move = "You slide the lantern to the side and bits of paint flake off from the bottom. This has been here for a while."

#################################################

lamp_look = "a lamp"
lamp_moved = "a lamp"
lamp_examine = "The lamp looks as if it has been handled recently, and has some areas where the dust is gone. You look inside and see a new lightbulb, which looks rather out of place considering the state and age of everything else in the room. You spot a burn mark on the back of the lamp shade."
lamp_examine_moved = "The lamp looks as if it has been handled recently, and has some areas where the dust is gone. You look inside and see a new lightbulb, which looks rather out of place considering the state and age of everything else in the room. On the front you see a large burn mark."
lamp_take = "No matter what you do, you are unable to take the lamp as it's cord goes into a hole in the wall."
lamp_move = "You turn the lamp around, and a large burn mark faces you."

#################################################
chair_look = "In the corner to your south-west there is a chair facing the wall. "
chair_moved = "In the corner to your south-west there is a chair which has been pulled away from the wall and turned to face you. "
chair_examine = "Likely a once used chair, it now looks quite unstable and would probably not hold anything past the dust that has settled apon it. It sits in the corner of the room "
chair_examine_moved = "Likely a once used chair, it now looks quite unstable and would probably not hold anything past the dust that has settled apon it. On the back a spot of bare and cracked wood is clearly visible where you touched it."
chair_take = "There is no way you will be able to carry this thing all over the place."
chair_move = "You slide the chair and turn it to face you."

#################################################
grate_look = "To your south you see a metal grate by the floor. Light is coming through and you smell fresh air."
grate_moved = "To your south you see a hole where the grate was by the floor. Light is coming through and you smell fresh air. The grate is bent back on the last remaining screw. "
grate_examine = "The grate is quite rusted but is still strong enough to stop you from passing. Three of the four screws are gone and it is just hanging onto one screw. the three empty screw holes are very marked up, almost as if someone removed them with something other than a screwdriver."
grate_examine_moved = "The grate has been folded back, bending the last screw. The screw is still holding on well, so you can't fully remove it. It is just enough to pass through."
grate_move = "You try your best but you fail to slide the grate. It is loose on one side though, so you may be able to pull on it."
grate_take = "The grate is screwed to the wall, how are you supposed to take it?"
grate_pull = "You pull hard on the grate and it starts to deform. You put your feet on the wall and give it your all. Suddenly the screw buckles and you are thrown back as you lose your grip. The passage is open!"

#################################################

note_look = ""
note_moved = ""
note_examine = ""
note_examine_moved = ""
note_move = ""
note_take = ""
note_pull = ""

stream_death = "The current is strong, and it sweeps you up by your feet and drags you across the rocks. You try to grab them but you are going too fast to get a hold. It finally pulls you under and you are unable to breathe."

intro = "----------------------------------------\nIn this game, you are trapped in a room,\nand need to find out how to leave. This\nprogram is highly inspired by similar\ngames such as Zork which was originally\nmade for the PDP10 mainframe by 4\nstudents at MIT around 1978. This\nprogram is meant to be used with a\n40-column display, but works fine on\nothers (just change the screen_size\nvariable in main.py).\nEnjoy! -Justin\n[help] - Display basic commands\n[start] - Start game\n[quit] - Quit game\n---------------------------------------"

help = "Help:\n\n[help] - Display commands\n[start] - Start game\n[quit] - Quit game\n[north] - Walk north\n[south] - Walk south\n[east] - Walk east\n[west] - Walk west\n[look] - Look around\nYou can also lift, and take items using:\n[lift (item)]\n[take (item)]"

logo = "  _____ _ _           _   _  __          \n / ____(_) |         | | | |/ /          \n| (___  _| | __ _ __ | |_| \' / __ _   _ \n \\___ \\| | |/_ \\ \'_ \\| __|  < /_ \\ | | |\n ____) | | | __/ | | | |_| . \\ __/ |_| |\n|_____/|_|_|\\__|_| |_|\\__|_|\\_\\__|\\__, |\n  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   __/ | \n  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  |___/ " #this mess is the ascii art. lots of escape characters!

compass = "\n\
  N\n\
W + E\n\
  S"

game_over = "\
===============\n\
|| GAME OVER ||\n\
===============\n"

helplist = ["=> help - Print help menu\n",
"=> quit - Quit game\n",
"=> north, n - Go north\n",
"=> south, s - Go south\n",
"=> east, e - Go east\n",
"=> west, w - Go west\n",
"=> inventory, i - Print inventory contents\n",
"=> take [item]- Take item (put it in inventory)\n",
"=> put [item] [in/on] [item]- Put item on/in table/container\n",
"=> look, l - Look around\n",
"=> examine [item] - Examine item\n",
"=> move [item] - Move item\n",
"=> pull [item] - Pull item\n",
"=> turn [on/off] [item] - Turn on or off ite\n",
"=> open [item] - Open item\n",
"=> close [item] - Close item\n",
"=> read [literature] - Read piece of literature"]