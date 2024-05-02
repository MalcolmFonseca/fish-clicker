import shop,gore,player,pygame,menuSystem,save,knife,sceneButton,bloodtemple,sigilMenu,bombSigil,bloodLightning,cursor,darkFamiliar,sigilInfoBox,hellFire

def init(current_screen):
    #event object for score update
    global UPDATE_SCORE
    UPDATE_SCORE = pygame.USEREVENT + 1
    #settings user can change
    global settings
    player_data = save.load_data()
    if player_data == False:
        #load default settings
        settings = {
            'Shop In Front':False
        }
    else:
        settings = player_data["settings"]

    #make game clock
    global clock
    clock = pygame.time.Clock()
    global clock_time
    clock_time = clock.tick(60)

    global running
    running = True

    #screen
    global screen 
    screen = current_screen
    global window_size
    window_size = screen.get_size()
    global scale
    scale = [window_size[0]/1920,window_size[1]/1080]

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

    #cursor
    global cursor_ob
    cursor_ob = cursor.Cursor()

    #gore
    global gore_ob
    gore_ob = gore.Gore()

    #knife
    global knife_ob
    knife_ob = knife.Knife()

    #bomb sigil
    global bomb_sigil
    bomb_sigil = bombSigil.BombSigil()

    #dark familiar
    global dark_familiar
    dark_familiar = darkFamiliar.DarkFamiliar()

    #blood lightning
    global blood_lightning
    blood_lightning = bloodLightning.BloodLightning()

    #hellfire
    global hell_fire
    hell_fire = hellFire.HellFire()

    #scenebutton
    global scene_button
    scene_button = sceneButton.SceneButton()

    #sigilmenu
    global sigil_menu
    sigil_menu = sigilMenu.SigilMenu()

    global sigil_info_box
    sigil_info_box = sigilInfoBox.SigilInfoBox()

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
    main_shop.update_unlocks()

def color_image(surface,current_color,wanted_color):
    var = pygame.PixelArray(surface)
    var.replace((current_color), wanted_color)
    del var