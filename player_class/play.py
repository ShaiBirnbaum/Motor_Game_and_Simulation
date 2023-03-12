from game_utils import utils

class Player: #all player functions and attributes
    def __init__(self, cash):
        self.cash = cash
        self.motorcycles = []
        # self.races = []
        # self.prizes = []

    def money_transaction(self, amount): #money transactions for buying motorcycles and winning/losing races.
        if self.cash + amount < 0:
            print("The motorcycle you chose is too expensive")
        else:
            self.cash = self.cash + amount
            print(f"**Your cash balance is now {format(self.cash, ',.2f')}**")
    
    def style_list(self, data):
        for el in data:
            print()
            bike_number = el.get('bike_number')
            print(f"bike_number:{bike_number}")
            for k, v in el.items():
                if k != 'bike_number':
                    if type(v) == int:
                        print(f"{k}:{v:,}")
                    else:
                        print(f"{k}:{v}")

    def show_garage(self): #shows all bought motorcycles
        print("\nTake a look at your new garage:\n")
        if self.motorcycles:
            self.style_list(self.motorcycles)
            
    def current_bike(self): #latest bought motorcycle- model name, top speed
        if self.motorcycles:
            current_bike_name = self.motorcycles[-1]['model_name']
            current_top_speed = self.motorcycles[-1]['top_speed']
            return (current_bike_name, current_top_speed)
        else:
            return None
        
    def id_to_marketplace_position(self, chosen_bike, data): #convert chosen bike number to current bike location in the marketplace
        counter=-1
        for mo in data:
            counter+=1
            if mo['bike_number'] == chosen_bike:
                return counter
        else:
            return None      

    def buy(self, chosen_bike, data): # buying a motorcycle
        market_position = self.id_to_marketplace_position(chosen_bike, data) #convert chosen bike number to its up to date marketplace position
        
        if market_position is None: #the bike number is not on the marketpplace
            print(f"There is no bike number {chosen_bike} in the marketplace. \nPlease try a different number.")
        #player has enough cash to buy the motorcycle
        elif data[market_position]["price"] < self.cash:
            print(f"\nWow!! you have just purchased {data[market_position]['model_name']}!!!")
            self.money_transaction((data[market_position]["price"])*(-1)) #substract motorcycle price
            self.motorcycles.append(data.pop(market_position)) #add motocycle to player, remove from marketplace
            self.current_bike()
            self.show_garage()    
        #bike is on the marketplace, but the player doesn't have enough cash to buy it.
        else: 
            print(f"You don't have enough cash to buy {data[market_position]['model_name']}")
                                                