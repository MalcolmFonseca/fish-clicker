import shop,gore,player,pygame,menuSystem,save,knife,sceneButton,bloodtemple

def init(current_screen):
    #event object for score update
    global UPDATE_SCORE
    UPDATE_SCORE = pygame.USEREVENT +1
    #settings user can change
    global settings
    player_data = save.load_data()
    if player_data == False:
        pass
    else:
        try:
            settings = player_data["settings"]
        except:
            settings = {
            'Shop In Front':False
        }

    #make game clock
    global clock
    clock = pygame.time.Clock()

    global running
    running = True
    #colors
    global light_water_color
    light_water_color = pygame.color.Color('#C0FDFB')
    global blue_color
    blue_color = pygame.color.Color('#B8E7E1')
    global sand_color
    sand_color = pygame.color.Color('#FFE5AD')
    global brown_color
    brown_color = pygame.color.Color('#D08C39')

    #screen
    global screen 
    screen = current_screen
    global window_size
    window_size = screen.get_size()

    #dict for num_to_word function
    global numwords
    numwords = {
        1e6:"Million",
        1e9:"Billion",
        1e12:"Trillion",
        1e15:"Quadrillion",
        1e18:"Quintillion",
        1e21:"Sextillion",
        1e24:"Septillion",
        1e27:"Octillion",
        1e30:"Nonillion",
        1e33:"Decillion"
    }

    #player
    global player_ob
    player_ob = player.Player()

    #shop
    global main_shop
    main_shop = shop.Shop()

    #menu system
    global menu_system
    menu_system = menuSystem.MenuSystem()

    #gore
    global gore_ob
    gore_ob = gore.Gore()

    #knife
    global knife_ob
    knife_ob = knife.Knife()

    #scenebutton
    global scene_button
    scene_button = sceneButton.SceneButton()

    #init bloodtemple scene
    bloodtemple.init()

def num_to_word(num):
    current_key = 1
    ending = ""
    for key in numwords:
        if num>=key:
            current_key = key
            ending = " " + numwords[key]
        else:
            break

    return_val = float(num/current_key) 
    return f'{str(round(return_val, 3) if return_val % 1 else int(return_val))} {ending}'

#function and event object to update score every 1 second
def update_score():
    player_ob.add_score(player_ob.sps)
    menu_system.update_unlocks()