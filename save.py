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
        "settings": util.settings
    }

    #write to json file
    with open("save.json","w") as f:
        json.dump(player_data,f)

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
