def add_bike_number(motor_list):
    counter=-1
    for mo in motor_list: 
        counter+=1
        mo["bike_number"]=counter
    marketplace = motor_list
    return marketplace

def style_dic_list(data):
    for bike in data:
        print()
        bike_number = bike.get('bike_number')
        print(f"bike_number:{bike_number}")
        for k, v in bike.items():
            if k != 'bike_number':
                if type(v)==int:
                    print(f"{k}:{v:,}")
                else:
                    print(f"{k}:{v}")
    
def simulate(data, rounds_number, race): 
    counter=0
    for i in range(1,rounds_number):
        counter+=1
        print(f"Round {counter}")
        race.all_competitors(data)
        if race.end_game() == "game over":
            break
        else:
            race.race_money()