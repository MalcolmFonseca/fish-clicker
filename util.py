import shop,pygame,gore,player

def init(current_screen):
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

    global main_shop
    main_shop = shop.Shop()

    #gore
    global gore_ob
    gore_ob = gore.Gore()
    

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