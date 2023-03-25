import enemy

class Round:
    
    def __init__(self):
        self.rounds = [(2, 100), (5, 50)] #add as many rounds as possible. First number represents num enemies, second number is delay

        self.num_enemies = 2
        self.delay = 10
        self.current_round = 0
    def next_round(self):
        
        self.num_enemies = self.rounds[self.current_round][0]
        self.delay = self.rounds[self.current_round][1]
        self.current_round += 1;
    def create_to_be_deployed(self):
        to_be_deployed = [];
        i = 0;
        while(i < self.num_enemies):
            to_be_deployed.append(enemy.Enemy());
            i += 1
        return to_be_deployed;