import pygame,time,shop,shopButton,player

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
player = player.Player()

#create main game shop
main_shop = shop.Shop(window_size)

#create shop buttons
seaweed_btn = shopButton.ShopButton("Seaweed",15,'Assets/seaweed.png')
seaslug_btn = shopButton.ShopButton("Seaslug",100,'Assets/seaslug.png')
crab_btn = shopButton.ShopButton("Crab",1_100,'Assets/crab.png')
angelfish_btn = shopButton.ShopButton("Angelfish",12_000,'Assets/angelfish.png')
clownfish_btn = shopButton.ShopButton("Clownfish",130_000,'Assets/clownfish.png')
squid_btn = shopButton.ShopButton("Squid",1_400_000,'Assets/squid.png')

#add buttons to main_shop
main_shop.all_buttons.append(seaweed_btn)
main_shop.all_buttons.append(seaslug_btn)
main_shop.all_buttons.append(crab_btn)
main_shop.all_buttons.append(angelfish_btn)
main_shop.all_buttons.append(clownfish_btn)
main_shop.all_buttons.append(squid_btn)
main_shop.all_buttons.append(seaweed_btn)

main_shop.current_buttons = main_shop.all_buttons

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

#create text for 
score_font = pygame.font.Font('Assets/Kamalla.ttf',80)
score_text = score_font.render('0',True,(0,0,0))
score_text_rect = score_text.get_rect()
score_text_rect.centerx = window_size[0]/3

#function to update score
def update_score():
    pass

#render method
def render():
    #render shop box
    pygame.draw.rect(screen,brown_color,main_shop.shop_rect)

    #render buttons
    position = 1
    for button in main_shop.current_buttons:
        button.position(position)
        position += 1
        pygame.draw.rect(screen,sand_color,button.button_rect)
        screen.blit(button.image,button.image_rect)
        screen.blit(button.name_text,button.name_text_rect)
        screen.blit(button.cost_text,button.cost_text_rect)

    #render arrows
    screen.blit(top_arrow,top_arrow_rect)
    screen.blit(bottom_arrow,bottom_arrow_rect)

    #render shop title and score text
    screen.blit(shop_title_text,shop_title_text_rect)
    screen.blit(score_text,score_text_rect)

    pygame.display.flip()

#update screen and set running to true
render()
running = True
#gameloop
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(.05)

pygame.quit()    