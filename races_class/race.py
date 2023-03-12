import random

class Races: #all races relevant functions and atributes
    def __init__(self, entry_fee, player):
        self.entry_fee = entry_fee #player fee for participation
        self.rivals = []
        self.player = player 
        self.player_bike = None
        self.competitors = [] 
        self.prize = entry_fee*4
        self.all_rounds = []

    def generate_rivals(self, data): #generate 3 random motorcycles to compete against
        rivals1=[]
        for i in range(3):          
            bikes_numbers = random.randint(0,len(data)-1)
            model_and_speed = (data[bikes_numbers]['model_name'], data[bikes_numbers]['top_speed'])
            rivals1.append(model_and_speed)
        return rivals1
    
    def end_game(self): #return game over when player doesnt have enough money for entry fee
        player_cash = self.player.cash
        entry_fee = self.entry_fee
        if player_cash < entry_fee:
            return "game over"


    def all_competitors(self, data): #combine rivals and players bike
        new_rivals = self.generate_rivals(data)
        last_bike = self.player.current_bike()
        
        if self.end_game() == "game over":
            print("Game Over")
        elif last_bike:
            new_rivals.append(last_bike)
            self.player_bike = last_bike
            self.competitors = new_rivals
        else:
            print("You Haven't Purchased a Bike Yet")
    
    def random_speed_boost(self, speed): #outputs random number between 0 and half the given motorcycles top_speed
        ran = random.randint(0, int(round(speed/(2/3))))
        return ran
    
    def save_round_details(self, competitors, win): #save the competitors and the winner of each round.
        last_round_details = []
        flag = False
        for i, j in competitors:
            if i == win and not flag:
                last_round_details.append((i + "- Winner", j))
                flag = True
            else:
                last_round_details.append((i, j))
        self.all_rounds.append(last_round_details)
    
    def winner(self): #which bike is the winner with the top speed?
        fastest = 0
        compete = self.competitors
        for m,s in compete:
            boost = self.random_speed_boost(s)
            if (s+boost) > fastest:
                fastest = s+boost
                winner = m
        self.save_round_details(compete, winner)
        return winner
     
    def race_money(self): #player looses entry fee or wins it *4
        if self.player.motorcycles==[]: #Checks if player has a bike
            print("You Haven't Purchased a Bike Yet") 
        elif self.end_game() == "game over": #Checks if player has enough cash to race
            print("Game Over") 
        else:
            winner = self.winner()
            print(f"The Winner Is {winner}!!!") #prints the winner
            if self.player_bike[0] == winner: #won> get money
                print(f"You have Won The Game!!!\n")
                self.player.money_transaction(self.prize) 
            else:
                print(f"You have Lost The Game!!!\n")
                self.player.money_transaction((self.entry_fee)*(-1)) #lost> pay entry fee

            
