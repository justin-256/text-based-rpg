########## OPTIONS: ##########
screen_size = 40
width = screen_size
developer_mode = False #turn on for debug settings: skips the menu and adds extra commands

if developer_mode == True:
    game_running = True
    player_location = [1,1]
else:
    game_running = False
    player_location = ["menu"]

#yes this should be a json or similar with no code. I was in a hurry and did not bother. there are not many things here, but in the future that is a must.