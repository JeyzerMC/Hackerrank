from functools import cmp_to_key
# MY CODE
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return '%s, %s' % (self.name, self.score)
        
    def comparator(self, b):
        if self.score > b.score:
            return -1
        elif self.score == b.score:
            if self.name > b.name:
                return 1
            else:
                return -1
        else:
            return 1
        
# BOILERPLATE CODE 
n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)