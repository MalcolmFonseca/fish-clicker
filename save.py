import json, os, io

def count_bought(shop):
    #make empty dict to be populated
    bought = {}

    for button in shop.all_buttons:
        bought[button.name] = button.owned

    return bought

def check_unlocked(shop):
    unlocked = {}

    for button in shop.all_buttons:
        unlocked[button.name] = button.unlocked

    return unlocked

def save_data(player_ob,shop):
    #create dict with player data
    player_data = {
        "score": player_ob.score,
        "total_score": player_ob.total_score,
        "sps": player_ob.sps,
        "kills": player_ob.kills,
        "bought": count_bought(shop),
        "unlocked": check_unlocked(shop)
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
