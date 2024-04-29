import util,pygame,background

def init():
    #temple
    global temple_image
    temple_image = pygame.image.load('Assets/temple/bloodtemple.png').convert_alpha()
    global temple_rect
    temple_rect = temple_image.get_rect()
    temple_image = pygame.transform.scale(temple_image,[temple_rect.width*util.scale[0],temple_rect.height*util.scale[1]])
    temple_rect = temple_image.get_rect()
    temple_rect.bottom = util.window_size[1]
    temple_rect.centerx = util.window_size[0]/2

    #book
    global book_image
    book_image = pygame.image.load('Assets/temple/book.png').convert_alpha()
    global book_rect
    book_rect = book_image.get_rect()
    book_image = pygame.transform.scale(book_image,[book_rect.width*util.scale[0],book_rect.height*util.scale[1]])
    book_rect = book_image.get_rect()
    book_rect.centerx = util.window_size[0]/2
    book_rect.centery = util.window_size[1]/3.5

def render():
    #render backdrop
    util.screen.blit(background.image,background.rect)

    #render temple
    util.screen.blit(temple_image,temple_rect)

    #render book
    util.screen.blit(book_image,book_rect)

    #position text
    util.player_ob.score_text_rect.centerx = util.window_size[0]/2
    util.player_ob.sps_text_rect.centerx = util.player_ob.score_text_rect.centerx

    #render score and sps text
    util.screen.blit(util.player_ob.score_text,util.player_ob.score_text_rect)
    util.screen.blit(util.player_ob.sps_text,util.player_ob.sps_text_rect)

    #render sigil menu if open
    if util.sigil_menu.enabled:
        util.sigil_menu.render()

    #render menu if any
    if util.menu_system.enabled:
        util.menu_system.render()
    #render menu button
    util.screen.blit(util.menu_system.menu_button,util.menu_system.menu_button_rect)

    #render bomb sigil
    if any(sigil.name == "Mass Hemorrhage" and sigil.bought for sigil in util.sigil_menu.all_sigils):
        util.bomb_sigil.render()

    #render knife button
    util.screen.blit(util.knife_ob.get_image(),util.knife_ob.rect)

    #render scene button
    util.screen.blit(util.scene_button.image,util.scene_button.rect)

    for group in util.gore_ob.gore_list:
        if pygame.sprite in group == False:
            util.gore_ob.gore_list.remove(group)
            continue
        group.update()

    #update creatures to respawn in background
    util.player_ob.bought.update()

    #update cursor
    util.cursor_ob.update()

    pygame.display.flip()

def enter():
    global running
    running = True
    while running:
        #event loop
        for event in pygame.event.get():
            #event check for score update    
            if event.type == util.UPDATE_SCORE:
                util.update_score()    
            if event.type == pygame.QUIT:
                util.running = False
                running = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: #handle player left click
                if util.menu_system.menu_button_rect.collidepoint(event.pos):
                    util.menu_system.toggle()
                    break
                if util.scene_button.rect.collidepoint(event.pos):
                    util.scene_button.press()
                    background.update()
                    running = False
                if book_rect.collidepoint(event.pos):
                    util.sigil_menu.enabled = True
                    break
                if util.knife_ob.rect.collidepoint(event.pos):
                    util.knife_ob.enabled = not util.knife_ob.enabled
                for sigil in util.sigil_menu.all_sigils:
                    if sigil.rect.collidepoint(event.pos):
                        sigil.buy()
                        break
                if util.sigil_menu.close_button_rect.collidepoint(event.pos):
                    util.sigil_menu.enabled = False
                    break
                if util.menu_system.enabled:
                    for button in util.menu_system.current_menu.buttons:
                        if button.rect.collidepoint(event.pos):
                            util.menu_system.current_menu.press(button)
                    for box in util.menu_system.current_menu.check_boxes:
                        if box.get_rect().collidepoint(event.pos):
                            util.menu_system.current_menu.check(box)
        render()
        util.clock.tick(60)