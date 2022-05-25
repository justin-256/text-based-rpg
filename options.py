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