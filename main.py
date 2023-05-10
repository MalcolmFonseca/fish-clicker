import pygame,time,shop,shopButton,player,math,creature

pygame.init()

#Initialize Game with light blue background
window_size = [1920,1055]
screen = pygame.display.set_mode(window_size)

#load palette
light_water_color = pygame.color.Color('#D4FAFC')
blue_color = pygame.color.Color('#B8E7E1')
sand_color = pygame.color.Color('#FFEEB3')
brown_color = pygame.color.Color('#9E6F21')

screen.fill(light_water_color)

#create player object
player_ob = player.Player()

#create main game shop
main_shop = shop.Shop(window_size)

#create shop buttons
seaweed_btn = shopButton.ShopButton("Seaweed",15,.1,'Assets/seaweed.png','stationary')
seaslug_btn = shopButton.ShopButton("Seaslug",100,1,'Assets/seaslug.png','walking')
crab_btn = shopButton.ShopButton("Crab",1_100,8,'Assets/crab.png','walking')
angelfish_btn = shopButton.ShopButton("Angelfish",12_000,47,'Assets/angelfish.png','swimming')
clownfish_btn = shopButton.ShopButton("Clownfish",130_000,260,'Assets/clownfish.png','swimming')
squid_btn = shopButton.ShopButton("Squid",1_400_000,1_400,'Assets/squid.png','swimming')
barracuda_btn = shopButton.ShopButton("Barracuda",1_400_000,1_400,'Assets/barracuda.png','swimming')
bluewhale_btn = shopButton.ShopButton("Blue Whale",1_400_000,1_400,'Assets/bluewhale.png','swimming')

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
            print("upworks")
    elif direction == "DOWN":
        #check if fully scrolled down
        if main_shop.current_position + 7 < len(main_shop.all_buttons) :
            main_shop.current_position += 7
            print("downworks")
    main_shop.current_buttons.clear()
    for i in range(main_shop.current_position,main_shop.current_position + 7):
        main_shop.current_buttons.append(main_shop.all_buttons[i])

#set current buttons
#main_shop.current_buttons = main_shop.all_buttons
move_shop("UP")

#create arrows for shop scrolling
top_arrow = pygame.image.load('Assets/arrow.png')
top_arrow_rect = top_arrow.get_rect()
top_arrow_rect.center = [seaweed_btn.button_rect.centerx,seaweed_btn.button_rect.top+15]

bottom_arrow = pygame.transform.rotate(top_arrow,180)
bottom_arrow_rect = bottom_arrow.get_rect()
bottom_arrow_rect.center = [seaweed_btn.button_rect.centerx,window_size[1]-35]

#create text for shop
title_font = pygame.font.Font('Assets/Kamalla.ttf',50)
shop_title_text = title_font.render('Shop',True,(0,0,0))
shop_title_text_rect = shop_title_text.get_rect()
shop_title_text_rect.left = seaweed_btn.button_rect.left
shop_title_text_rect.top = 5

#create text for score
score_font = pygame.font.Font('Assets/Kamalla.ttf',80)
score_text = score_font.render(f'Chum: {math.trunc(player_ob.score)}',True,(0,0,0))
score_text_rect = score_text.get_rect()
score_text_rect.centerx = window_size[0]/3

#function and event object to update score every 1 second
UPDATE_SCORE = pygame.USEREVENT +1
def update_score():
    player_ob.score += player_ob.sps
    global score_text
    score_text = score_font.render(f'Chum: {math.trunc(player_ob.score)}',True,(0,0,0))

def buy(button):
    player_ob.score -+ button.cost
    player_ob.sps += button.sps
    player_ob.bought.add(button.buy())

#render method
def render():
    #render backdrop
    screen.fill(light_water_color)
    #render shop box
    pygame.draw.rect(screen,brown_color,main_shop.shop_rect)

    #render buttons
    position = 1
    for button in main_shop.current_buttons:
        button.position(position)
        position += 1
        pygame.draw.rect(screen,sand_color,button.button_rect)
        #check if cost should be red
        button.check_expensive(player_ob.score)
        screen.blit(button.image,button.image_rect)
        screen.blit(button.name_text,button.name_text_rect)
        screen.blit(button.cost_text,button.cost_text_rect)
        screen.blit(button.owned_text,button.owned_text_rect)

    #render arrows
    screen.blit(top_arrow,top_arrow_rect)
    screen.blit(bottom_arrow,bottom_arrow_rect)

    #render shop title
    screen.blit(shop_title_text,shop_title_text_rect)

    #render all owned creatures
    player_ob.bought.update()
    player_ob.bought.draw(screen)

    #render score text
    screen.blit(score_text,score_text_rect)

    pygame.display.flip()

#make game clock
clock = pygame.time.Clock()

#update player score every 1 second
pygame.time.set_timer(UPDATE_SCORE,1000)

#update screen and set running to true
render()
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
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: #handle player purchases from the shop
            for button in main_shop.current_buttons:
                if button.button_rect.collidepoint(event.pos):
                    buy(button)
            if top_arrow_rect.collidepoint(event.pos):
                move_shop("UP")
            if bottom_arrow_rect.collidepoint(event.pos):
                move_shop("DOWN")
                    
    render()
    clock.tick(30)

pygame.quit()    