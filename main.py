import pygame,time,shop,shopButton

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

#create main game shop
main_shop = shop.Shop(window_size)

#create shop buttons
seaweed_btn = shopButton.ShopButton("Seaweed",15,None)

def render():
    #render shop box
    pygame.draw.rect(screen,sand_color,main_shop.shop_rect)

    #render buttons
    pygame.draw.rect(screen,brown_color,seaweed_btn.button_rect)

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