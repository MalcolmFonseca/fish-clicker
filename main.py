import pygame,shopButton,util,save,background

pygame.init()

#set fullscreen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

util.init(screen)
background.init()

#create dictionary storing pricing tiers for easier changes down the line
#format is cost:sps
price_dict = {
    15:.1,
    100:1,
    1_100:8,
    12_000:47,
    130_000:260,
    1.4e6:1_400,
    20e6:7_800,
    330e6:44_000,
    5.1e9:260_000,
    75e9:1.6e6,
    1e12:10e6,
    14e12:65e6,
    170e12:430e6,
    2.1e15:2.9e9,
    26e15:21e9,
    310e15:150e9,
    71e18:1.1e12,
    12e21:8.3e12,
    1.9e24:64e12,
    540e27:510e12
}

price_keys = list(price_dict.keys())

#create shop buttons
seaweed_btn = shopButton.ShopButton("Seaweed",price_keys[0],price_dict[price_keys[0]],'stationary','Assets/fishimages/seaweed.png','Assets/shopicons/seaweedShop.png')
coral_btn = shopButton.ShopButton("Coral",price_keys[1],price_dict[price_keys[1]],'stationary','Assets/fishimages/coral.png','Assets/shopicons/coralShop.png')
seaslug_btn = shopButton.ShopButton("Seaslug",price_keys[2],price_dict[price_keys[2]],'walking','Assets/fishimages/seaslug.png','Assets/shopicons/seaslugShop.png')
seahorse_btn = shopButton.ShopButton("Sea Horse",price_keys[3],price_dict[price_keys[3]],'swimming','Assets/fishimages/seahorse.png','Assets/shopicons/seahorseShop.png')
crab_btn = shopButton.ShopButton("Crab",price_keys[4],price_dict[price_keys[4]],'walking','Assets/fishimages/crab.png','Assets/shopicons/crabShop.png')
angelfish_btn = shopButton.ShopButton("Angelfish",price_keys[5],price_dict[price_keys[5]],'swimming','Assets/fishimages/angelfish.png','Assets/shopicons/angelfishShop.png')
clownfish_btn = shopButton.ShopButton("Clownfish",price_keys[6],price_dict[price_keys[6]],'swimming','Assets/fishimages/clownfish.png','Assets/shopicons/clownfishShop.png')
cuttlefish_btn = shopButton.ShopButton("Cuttlefish",price_keys[7],price_dict[price_keys[7]],'swimming','Assets/fishimages/cuttlefish.png','Assets/shopicons/cuttlefishShop.png')
squid_btn = shopButton.ShopButton("Squid",price_keys[8],price_dict[price_keys[8]],'swimming','Assets/fishimages/squid.png','Assets/shopicons/squidShop.png')
barracuda_btn = shopButton.ShopButton("Barracuda",price_keys[9],price_dict[price_keys[9]],'swimming','Assets/fishimages/barracuda.png','Assets/shopicons/barracudaShop.png')
bluewhale_btn = shopButton.ShopButton("Blue Whale",price_keys[10],price_dict[price_keys[10]],'swimming','Assets/fishimages/bluewhale.png','Assets/shopicons/bluewhaleShop.png')

#make function for scrolling through shop
def move_shop(direction):
    if direction == "UP":
        #check if fully scrolled up
        if util.main_shop.current_position != 0 :
            util.main_shop.current_position -= 7
    elif direction == "DOWN":
        #check if fully scrolled down
        if util.main_shop.current_position + 7 < len(util.main_shop.unlocked_buttons) :
            util.main_shop.current_position += 7
    update_buttons()
    position_buttons()

def update_buttons():
    util.main_shop.current_buttons.clear()
    for i in range(util.main_shop.current_position,util.main_shop.current_position + 7):
        try:
            util.main_shop.current_buttons.append(util.main_shop.unlocked_buttons[i])
        except: #will stop adding buttons when no more are available
            break

def position_buttons():
    position = 1
    for button in util.main_shop.current_buttons:
        button.position(position)
        position += 1

#set current buttons
move_shop("UP")

#position shop buttons
util.main_shop.title_text_rect.left = seaweed_btn.button_rect.left
util.main_shop.top_arrow_rect.center = [seaweed_btn.button_rect.centerx,util.window_size[1]/31]
util.main_shop.bottom_arrow_rect.center = [seaweed_btn.button_rect.centerx,util.window_size[1]-util.window_size[1]/31]

#create buttons for minimizing shop
open_shop_button_image = pygame.image.load('Assets/openShop.png').convert()
open_shop_button_rect = open_shop_button_image.get_rect()
close_shop_button_image = pygame.image.load('Assets/closeShop.png').convert()
close_shop_button_rect = close_shop_button_image.get_rect()
#position each button
open_shop_button_rect.right = util.window_size[0] - util.window_size[0]/128
open_shop_button_rect.top = util.window_size[1]/128
close_shop_button_rect.right = open_shop_button_rect.right
close_shop_button_rect.top = open_shop_button_rect.top

#create button for menu
menu_button = pygame.image.load('Assets/menu.png').convert()
menu_button_rect = menu_button.get_rect()
menu_button_rect.top = util.window_size[1]/128
menu_button_rect.left = util.window_size[1]/128

#function and event object to update score every 1 second
UPDATE_SCORE = pygame.USEREVENT +1
def update_score():
    util.player_ob.add_score(util.player_ob.sps)
    update_unlocks()
##################################################################### LOADING DATA
def load_purchases(player_data):
    for button in util.main_shop.all_buttons:
        #load
        try:
            button.owned = player_data["bought"][f"{button.name}"]
        except:
            button.owned = 0
        #create all bought creatures
        for n in range(0,button.owned):
            util.player_ob.bought.add(button.add())

def load_unlocks(player_data):
    util.main_shop.unlocked_buttons.clear()
    for button in util.main_shop.all_buttons:
        #load save
        try:
            button.unlocked = player_data["unlocked"][f"{button.name}"]
        except:
            button.unlocked = False

        #unlock button if already unlocked
        if button.unlocked == True:
            util.main_shop.unlocked_buttons.append(button)
            update_buttons()
            position_buttons()

def load_player(player_data):
    try:
        util.player_ob.score = player_data["score"]
        util.player_ob.total_score = player_data["total_score"]
        util.player_ob.sps = player_data["sps"]
        util.player_ob.kills = player_data["kills"]
    except:
        pass

def load_data(player_data):
    if player_data == False:
        pass
    else:
        load_purchases(player_data)
        load_unlocks(player_data)
        load_player(player_data)
#####################################################################
def update_unlocks():
    for button in util.main_shop.all_buttons:
        if button.check_unlock():
            util.main_shop.unlocked_buttons.append(button)
            update_buttons()
            position_buttons()

def buy(button):
    util.player_ob.add_score(-button.cost)
    util.player_ob.add_sps(button.sps)
    util.player_ob.bought.add(button.buy())
    position_buttons()

def toggle_shop():
    #simple invert so as to not have to write another if, too many as is
    util.main_shop.minimize = not util.main_shop.minimize

    #reposition text
    if util.main_shop.minimize:
        util.main_shop.title_text_rect.right = close_shop_button_rect.left - util.window_size[0]/128
    else:
        util.main_shop.title_text_rect.left = seaweed_btn.button_rect.left

#render method
def render():
    #render backdrop
    screen.blit(background.image,background.rect)

    #position sps text
    util.player_ob.sps_text_rect.centerx = util.player_ob.score_text_rect.centerx

    #render all owned creatures
    util.player_ob.bought.update()
    for creature in util.player_ob.bought:
        if creature.dead == False:
            screen.blit(creature.image,creature.rect)

    #render gore
    for group in util.gore_ob.gore_list:
        if pygame.sprite in group == False:
            util.gore_ob.gore_list.remove(group)
            continue
        group.update()
        for blood in group:
            pygame.draw.rect(screen,'#D40404',blood.rect)

    #render score and sps text
    screen.blit(util.player_ob.score_text,util.player_ob.score_text_rect)
    screen.blit(util.player_ob.sps_text,util.player_ob.sps_text_rect)

    #render menu if any
    if util.menu_system.enabled:
        util.menu_system.render()

    #render menu button
    screen.blit(menu_button,menu_button_rect)
    #check if shop is minimized
    if util.main_shop.minimize:
        #position score text
        util.player_ob.score_text_rect.centerx = util.window_size[0]/2

        #render maximize button
        screen.blit(open_shop_button_image,open_shop_button_rect)
    else:
        #position score text
        util.player_ob.score_text_rect.centerx = util.window_size[0]/3

        util.main_shop.render()
    
        #render minimize button
        screen.blit(close_shop_button_image,close_shop_button_rect)

    pygame.display.flip()

#make game clock
clock = pygame.time.Clock()

#update player score every 1 second
pygame.time.set_timer(UPDATE_SCORE,1000)

#update screen, load data
load_data(save.load_data())
render()
update_score()
background.update()
#gameloop
while util.running:
    #event loop
    for event in pygame.event.get():
        #event check for score update    
        if event.type == UPDATE_SCORE:
            update_score()    
        if event.type == pygame.QUIT:
            util.running = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: #handle player left click
            if menu_button_rect.collidepoint(event.pos):
                        util.menu_system.toggle()
                        break   
            if util.menu_system.enabled:
                for button in util.menu_system.current_menu.buttons:
                    if button.rect.collidepoint(event.pos):
                        util.menu_system.current_menu.press(button)
            else:
                for button in util.main_shop.current_buttons:
                    if button.button_rect.collidepoint(event.pos) and util.main_shop.minimize == False:
                        #if util.player_ob.score > button.cost: #comment out for free shop creatures
                            buy(button)
                            break         
            if util.main_shop.top_arrow_rect.collidepoint(event.pos) and util.main_shop.minimize == False:
                move_shop("UP")
                break
            if util.main_shop.bottom_arrow_rect.collidepoint(event.pos) and util.main_shop.minimize == False:
                move_shop("DOWN")
                break
            if close_shop_button_rect.collidepoint(event.pos):
                toggle_shop()
                break        
    render()
    clock.tick(30)

pygame.quit()    