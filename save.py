import json, os, io, util

def count_bought():
    #make empty dict to be populated
    bought = {}

    for button in util.main_shop.all_buttons:
        bought[button.name] = button.owned

    return bought

def check_unlocked():
    unlocked = {}

    for button in util.main_shop.all_buttons:
        unlocked[button.name] = button.unlocked

    return unlocked

def check_sigils():
    sigils = {}

    for sigil in util.sigil_menu.all_sigils:
        sigils[sigil.name] = sigil.bought

    return sigils

def save_data():
    #create dict with player data
    player_data = {
        "score": util.player_ob.score,
        "total_score": util.player_ob.total_score,
        "sps": util.player_ob.sps,
        "kills": util.player_ob.kills,
        "blood": util.player_ob.blood,
        "bought": count_bought(),
        "unlocked": check_unlocked(),
        "sigils": check_sigils(), 
        "ascensions": util.player_ob.ascensions,
        "settings": util.settings
    }

    try:
        #write to json file
        with open("save.json","w") as f:
            json.dump(player_data,f)
        util.popups.create_popup("Game Saved")
    except:
        util.popups.create_popup("Error Saving Game")

def load_data():
    #check if file exists
    if os.path.isfile("save.json") and os.access("save.json", os.R_OK):
        pass
    else:
        #create new file
        with io.open(os.path.join("save.json"), 'w') as db_file:
            db_file.write(json.dumps({}))
        
        return False

    #read from json file
    with open("save.json","r") as f:
        player_data = json.load(f)

    return player_data

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
            util.main_shop.update_buttons()
            util.main_shop.position_buttons()

def load_player(player_data):
    try:
        util.player_ob.score = player_data["score"]
        util.player_ob.total_score = player_data["total_score"]
        util.player_ob.sps = player_data["sps"]
        #render sps text before screen shows
        util.player_ob.add_sps(0)
        util.player_ob.kills = player_data["kills"]
        util.player_ob.blood = player_data["blood"]
    except:
        pass

def load_sigils(player_data):
    for sigil in util.sigil_menu.all_sigils:
        try:
            sigil.bought = player_data["sigils"][f"{sigil.name}"]
        except:
            sigil.bought = False

def load(player_data):
    if player_data == False:
        pass
    else:
        load_purchases(player_data)
        load_unlocks(player_data)
        load_player(player_data)
        load_sigils(player_data)