import util,pygame,main,background

def render():
    #render backdrop
    util.screen.blit(background.image,background.rect)

    #position sps text
    util.player_ob.sps_text_rect.centerx = util.player_ob.score_text_rect.centerx

    #render score and sps text
    util.screen.blit(util.player_ob.score_text,util.player_ob.score_text_rect)
    util.screen.blit(util.player_ob.sps_text,util.player_ob.sps_text_rect)

    #render menu if any
    if util.menu_system.enabled:
        util.menu_system.render()
    #render menu button
    util.screen.blit(main.menu_button,main.menu_button_rect)

    pygame.display.flip()

def enter():
    while util.running:
        #event loop
        for event in pygame.event.get():
            #event check for score update    
            if event.type == main.UPDATE_SCORE:
                main.update_score()    
            if event.type == pygame.QUIT:
                util.running = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: #handle player left click
                if main.menu_button_rect.collidepoint(event.pos):
                    util.menu_system.toggle()
                    break
                if util.menu_system.enabled:
                    for button in util.menu_system.current_menu.buttons:
                        if button.rect.collidepoint(event.pos):
                            util.menu_system.current_menu.press(button)
                    for box in util.menu_system.current_menu.check_boxes:
                        if box.get_rect().collidepoint(event.pos):
                            util.menu_system.current_menu.check(box)
        render()
        main.clock.tick(30)