import enemy
import random
class Round:
    
    def __init__(self):
        self.rounds = [[{"Norm": 5}, 50],[{"Norm":3, "Tank": 1}, 40] ,[{"Fast":1, "Norm": 4}, 20]] #add as many rounds as possible. Dictionary is the type: quantity, second number is delay

        self.num_enemies = 2
        self.delay = 10
        self.current_round = 0
        self.to_be_deployed = []
    def next_round(self):
        type_list = list(self.rounds[self.current_round][0].keys());
        self.delay = self.rounds[self.current_round][1]
        self.to_be_deployed = []
        while(bool(self.rounds[self.current_round][0])): #while there are still enemies in the dictionary
            rand = random.randint(0, len(type_list) - 1);
            if(type_list[rand] == 'Fast'):
                self.to_be_deployed.append(enemy.Fast_enemy())
            if(type_list[rand] == 'Norm'):
                self.to_be_deployed.append(enemy.Enemy())
            if(type_list[rand] == 'Tank'):
                self.to_be_deployed.append(enemy.Tank_enemy())
            self.rounds[self.current_round][0][type_list[rand]] -= 1
            if(self.rounds[self.current_round][0][type_list[rand]] == 0):
                self.rounds[self.current_round][0].pop(type_list[rand])
                type_list.remove(type_list[rand])
        self.current_round += 1
        
    def create_to_be_deployed(self):
        
        return self.to_be_deployed;