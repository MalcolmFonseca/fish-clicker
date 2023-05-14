import pygame,shop,shopButton,player,math,settings,menu,borderedRect

pygame.init()

#set fullscreen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#sync settings between classes
settings.init(screen.get_size())

#load palette
light_water_color = pygame.color.Color('#C0FDFB')
blue_color = pygame.color.Color('#B8E7E1')
sand_color = pygame.color.Color('#FFE5AD')
brown_color = pygame.color.Color('#D08C39')

#create player object
player_ob = player.Player()

#create main game shop
main_shop = shop.Shop()

#create shop buttons
seaweed_btn = shopButton.ShopButton("Seaweed",15,.1,'stationary','Assets/fishimages/seaweed.png','Assets/shopicons/seaweedShop.png')
seaslug_btn = shopButton.ShopButton("Seaslug",100,1,'walking','Assets/fishimages/seaslug.png','Assets/shopicons/seaslugShop.png')
crab_btn = shopButton.ShopButton("Crab",1_100,8,'walking','Assets/fishimages/crab.png','Assets/shopicons/crabShop.png')
angelfish_btn = shopButton.ShopButton("Angelfish",12_000,47,'swimming','Assets/fishimages/angelfish.png','Assets/shopicons/angelfishShop.png')
clownfish_btn = shopButton.ShopButton("Clownfish",130_000,260,'swimming','Assets/fishimages/clownfish.png','Assets/shopicons/clownfishShop.png')
squid_btn = shopButton.ShopButton("Squid",1_400_000,1_400,'swimming','Assets/fishimages/squid.png','Assets/shopicons/squidShop.png')
barracuda_btn = shopButton.ShopButton("Barracuda",1_400_000,1_400,'swimming','Assets/fishimages/barracuda.png','Assets/shopicons/barracudaShop.png')
bluewhale_btn = shopButton.ShopButton("Blue Whale",1_400_000,1_400,'swimming','Assets/fishimages/bluewhale.png','Assets/shopicons/bluewhaleShop.png')

#add buttons to main_shop
main_shop.all_buttons.append(seaweed_btn)
main_shop.all_buttons.append(seaslug_btn)
main_shop.all_buttons.append(crab_btn)
main_shop.all_buttons.append(angelfish_btn)
main_shop.all_buttons.append(clownfish_btn)
main_shop.all_buttons.append(squid_btn)
main_shop.all_buttons.append(barracuda_btn)
main_shop.all_buttons.append(bluewhale_btn)

#make function for scrolling through shop
def move_shop(direction):
    if direction == "UP":
        #check if fully scrolled up
        if main_shop.current_position != 0 :
            main_shop.current_position -= 7
    elif direction == "DOWN":
        #check if fully scrolled down
        if main_shop.current_position + 7 < len(main_shop.unlocked_buttons) :
            main_shop.current_position += 7
    update_buttons()
    position_buttons()

def update_buttons():
    main_shop.current_buttons.clear()
    for i in range(main_shop.current_position,main_shop.current_position + 7):
        try:
            main_shop.current_buttons.append(main_shop.unlocked_buttons[i])
        except: #will stop adding buttons when no more are available
            break

def position_buttons():
    position = 1
    for button in main_shop.current_buttons:
        button.position(position)
        position += 1

#set current buttons
move_shop("UP")

#create arrows for shop scrolling
top_arrow = pygame.image.load('Assets/arrow.png')
top_arrow_rect = top_arrow.get_rect()
top_arrow_rect.center = [seaweed_btn.button_rect.centerx,settings.window_size[1]/31]

bottom_arrow = pygame.transform.rotate(top_arrow,180)
bottom_arrow_rect = bottom_arrow.get_rect()
bottom_arrow_rect.center = [seaweed_btn.button_rect.centerx,settings.window_size[1]-settings.window_size[1]/31]

#create text for shop
title_font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(settings.window_size[1]/22))
shop_title_text = title_font.render('Shop',True,(0,0,0))
shop_title_text_rect = shop_title_text.get_rect()
shop_title_text_rect.left = seaweed_btn.button_rect.left
shop_title_text_rect.top = 5

#create text for score
score_font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(settings.window_size[1]/13.5))
score_text = score_font.render(f'Chum: {math.trunc(player_ob.score)}',True,(0,0,0))
score_text_rect = score_text.get_rect()
score_text_rect.centerx = settings.window_size[0]/3

#create text for sps
sps_font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(settings.window_size[1]/20))
sps_text = sps_font.render(f'Cps: {player_ob.sps:.1f}',True,(0,0,0))
sps_text_rect = sps_text.get_rect()
sps_text_rect.centerx = score_text_rect.centerx
sps_text_rect.top = score_text_rect.bottom

#create buttons for minimizing shop
open_shop_button_image = pygame.image.load('Assets/openShop.png')
open_shop_button_rect = open_shop_button_image.get_rect()
close_shop_button_image = pygame.image.load('Assets/closeShop.png')
close_shop_button_rect = close_shop_button_image.get_rect()
#position each button
open_shop_button_rect.right = settings.window_size[0] - settings.window_size[0]/128
open_shop_button_rect.top = settings.window_size[1]/128
close_shop_button_rect.right = open_shop_button_rect.right
close_shop_button_rect.top = open_shop_button_rect.top

#create minimized shop box
minimized_shop_rect = borderedRect.bordered_rect(close_shop_button_rect.left - settings.window_size[0]/64 - shop_title_text_rect.width,0,settings.window_size[0]-shop_title_text_rect.left,top_arrow_rect.height + settings.window_size[1]/90,settings.window_size[0]/384,brown_color,(0,0,0))

#create button for menu
menu_button = pygame.image.load('Assets/menu.png')
menu_button_rect = menu_button.get_rect()
menu_button_rect.top = settings.window_size[1]/128
menu_button_rect.left = settings.window_size[1]/128
#create menus
main_menu = menu.MainMenu()

#function and event object to update score every 1 second
UPDATE_SCORE = pygame.USEREVENT +1
def update_score():
    player_ob.score += player_ob.sps
    player_ob.total_score += player_ob.sps
    #remake text
    global score_text
    score_text = score_font.render(f'Chum: {math.trunc(player_ob.score)}',True,(0,0,0))
    global score_text_rect
    score_text_rect = score_text.get_rect()
    update_unlocks()

def update_unlocks():
    for button in main_shop.all_buttons:
        if button.check_unlock(player_ob.total_score):
            main_shop.unlocked_buttons.append(button)
            update_buttons()
            position_buttons()

def buy(button):
    player_ob.score -= button.cost
    player_ob.sps += button.sps
    player_ob.bought.add(button.buy())
    #update text immediately for more responsive gameplay
    global score_text
    score_text = score_font.render(f'Chum: {math.trunc(player_ob.score)}',True,(0,0,0))
    global sps_text
    sps_text = sps_font.render(f'Cps: {player_ob.sps:.1f}',True,(0,0,0))
    position_buttons()

def click_creature():
    player_ob.score += 1
    player_ob.total_score += 1
    #update text immediately for more responsive gameplay
    global score_text
    score_text = score_font.render(f'Chum: {math.trunc(player_ob.score)}',True,(0,0,0))
    #display effect to show user their clicks are working
    pygame.mouse.get_pos

def toggle_shop():
    #simple invert so as to not have to write another if, too many as is
    main_shop.minimize = not main_shop.minimize

    #reposition text
    if main_shop.minimize:
        shop_title_text_rect.right = close_shop_button_rect.left - settings.window_size[0]/128
    else:
        shop_title_text_rect.left = seaweed_btn.button_rect.left
        

#render method
def render():
    #render backdrop
    screen.fill(light_water_color)

    #check if shop is minimized
    if main_shop.minimize:
        #position score text
        score_text_rect.centerx = settings.window_size[0]/2

        #render minimized shop box
        pygame.draw.rect(screen,minimized_shop_rect.border_color,minimized_shop_rect.border_rect)
        pygame.draw.rect(screen,minimized_shop_rect.inner_color,minimized_shop_rect.inner_rect)

        #render minimize button
        screen.blit(open_shop_button_image,open_shop_button_rect)
    else:
        #position score text
        score_text_rect.centerx = settings.window_size[0]/3
        if main_menu.enabled:
            score_text_rect.centerx = settings.window_size[0]/2

        #render shop box
        pygame.draw.rect(screen,main_shop.shop_rect.border_color,main_shop.shop_rect.border_rect)
        pygame.draw.rect(screen,main_shop.shop_rect.inner_color,main_shop.shop_rect.inner_rect)
    
        #render minimize button
        screen.blit(close_shop_button_image,close_shop_button_rect)

        #render item buttons
        for button in main_shop.current_buttons:
            pygame.draw.rect(screen,sand_color,button.button_rect)
            #check if cost should be red
            button.check_expensive(player_ob.score)

            screen.blit(button.icon_image,button.icon_image_rect)
            screen.blit(button.name_text,button.name_text_rect)
            screen.blit(button.cost_text,button.cost_text_rect)
            screen.blit(button.owned_text,button.owned_text_rect)
            screen.blit(button.sps_text,button.sps_text_rect)
        
        #render arrows
        screen.blit(top_arrow,top_arrow_rect)
        screen.blit(bottom_arrow,bottom_arrow_rect)

    #position sps text
    sps_text_rect.centerx = score_text_rect.centerx

    #render shop title
    screen.blit(shop_title_text,shop_title_text_rect)

    #render all owned creatures
    player_ob.bought.update()
    player_ob.bought.draw(screen)

    #render score and sps text
    screen.blit(score_text,score_text_rect)
    screen.blit(sps_text,sps_text_rect)

    #render menu if any
    render_menu()

    #render menu button
    screen.blit(menu_button,menu_button_rect)

    pygame.display.flip()

def render_menu():
    if main_menu.enabled:

        #draw menu box
        pygame.draw.rect(screen,main_menu.menu_rect.border_color,main_menu.menu_rect.border_rect)
        pygame.draw.rect(screen,main_menu.menu_rect.inner_color,main_menu.menu_rect.inner_rect)

        #render exit button
        pygame.draw.rect(screen,sand_color,main_menu.exit_button_rect)
        screen.blit(main_menu.exit_text,main_menu.exit_text_rect)

#make game clock
clock = pygame.time.Clock()

#update player score every 1 second
pygame.time.set_timer(UPDATE_SCORE,1000)

#update screen and set running to true
render()
update_score()
running = True
#gameloop
while running:
    #event loop
    for event in pygame.event.get():
        #event check for score update    
        if event.type == UPDATE_SCORE:
            update_score()    
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: #handle player left click
            if main_menu.exit_button_rect.collidepoint(event.pos) and main_menu.enabled:
                running = False
            if top_arrow_rect.collidepoint(event.pos) and main_shop.minimize == False:
                move_shop("UP")
                break
            if bottom_arrow_rect.collidepoint(event.pos) and main_shop.minimize == False:
                move_shop("DOWN")
                break
            if close_shop_button_rect.collidepoint(event.pos):
                toggle_shop()
                break
            for owned_creature in player_ob.bought:
                if owned_creature.rect.collidepoint(event.pos):
                    click_creature()
                    break
            for button in main_shop.current_buttons:
                if button.button_rect.collidepoint(event.pos) and main_shop.minimize == False:
                    #if player_ob.score > button.cost: #comment out for free shop creatures
                        buy(button)
                        break
            if menu_button_rect.collidepoint(event.pos):
                    main_menu.enabled = not main_menu.enabled
                    break            
                    
    render()
    clock.tick(30)

pygame.quit()    