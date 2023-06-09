import enemy
import random
class Round:
    
    def __init__(self):
        self.rounds = [[{"Norm": 9}, 100],[{"Norm":9, "Fast": 1}, 70],
        [{"Norm":8, "Fast":2}, 50], [{"Norm": 8, "Fast":2}, 20], 
        [{"Tank":5}, 40], [{"Norm": 6, "Tank": 3, "Fast": 3}, 40], 
        [{"Norm": 4, "Tank": 3, "Fast": 5}, 30], [{"Norm": 4, "Tank": 5, "Fast": 7}, 30], [{"Fast": 15}, 30], [{"Norm": 5, "Tank": 8, "Fast": 9}, 20],
        [{"Norm": 5, "Tank": 7, "Fast": 12}, 10], [{"Norm": 5, "Tank": 3, "Fast": 18, "super_fast":2}, 10], [{"Norm": 3, "Tank": 10, "Fast":8, "super_tank": 2, "super_fast": 2}, 10],
        [{"Norm": 1, "Tank": 15, "Fast":20, "super_tank": 4, "super_fast":4}, 10]
        ]  #add as many rounds as possible. Dictionary is the type: quantity, second number is delay

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
            if(type_list[rand] == 'super_fast'):
                self.to_be_deployed.append(enemy.super_fast())
            if(type_list[rand] == "super_tank"):
                self.to_be_deployed.append(enemy.super_tank())
            self.rounds[self.current_round][0][type_list[rand]] -= 1
            if(self.rounds[self.current_round][0][type_list[rand]] == 0):
                self.rounds[self.current_round][0].pop(type_list[rand])
                type_list.remove(type_list[rand])
        self.current_round += 1
        
    def create_to_be_deployed(self):
        
        return self.to_be_deployed;