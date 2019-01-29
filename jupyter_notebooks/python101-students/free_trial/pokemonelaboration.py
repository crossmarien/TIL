class Pokemon:
    def __init__(self, level):
        self.level = level
        self.hp = self.level * 10
        
    def set_hp(self, point):
        self.hp += point
        
    def check_status(self):
        if self.hp > 0:
            return True
        else: 
            return False
        
    def print_status(self):
        print(f'{self.name} 의 체력: {self.hp}')
        
       
    
    
    
    
import random
class Pikachu(Pokemon):
    # Pokemon 클래스 상속으로 다 물려받음!
    # def __init__(self, name, level):
    #     self.name = name
    #     self.level = level
    #     self.hp = level * 10
        
    # def set_hp(self, point):
    #     self.hp += point
        
    # def check_status(self):
    #     if self.hp > 0:
    #         return True
    #     else: 
    #         return False
        
    name = '피카츄'
    types = ('elec')
    def body_attack(self, enemy):
        enemy.set_hp(-1 * self.level)
        
    def thousand_volt(self, enemy):
        if 'water' in enemy.types:
            enemy.set_hp(-1.3 * self.level)
            print('효과는 굉장했다!')
        else:
            enemy.set_hp(-1.05 * self.level)
            
    def attack(self, enemy):
        c = random.choice([1, 2])
        if c == 1:
            self.body_attack(enemy)
        else:
            self.thousand_volt(enemy)
            
class Squirtle(Pokemon):
    name = '꼬부기'
    types = ('water')
    def body_attack(self, enemy):
        enemy.set_hp(-0.98 * self.level)
    
    def water_attack(self, enemy):
        enemy.set_hp(-1.08 * self.level)
    
    def attack(self, enemy):
        c = random.choice([1, 2])
        if c == 1:
            self.body_attack(enemy)
        else:
            self.water_attack(enemy)
            
            
            

            
            
            
            
a = Pikachu(10)
b = Squirtle(10)

def battle(p1, p2):
    import random
    # 선공 후공 결정
    vs = [p1, p2]
    random.shuffle(vs)
    winner = 0
    prev, after = tuple(vs)
    while prev.check_status() and after.check_status():
        if prev.check_status:
            prev.attack(after)
            prev.print_status()
        else:
            winner = after
            break
        if after.check_status():
            after.attack(prev)
            after.print_status()
        else:
            winner = prev
            break
            
    print(f'{winner.name} 의 승리!')
    
# battle(Pikachu(20), Squirtle(21))


your_pokemon={Pikachu:20}
wild_pokemon=['Pikachu','Squirtle']

def go_pikachu():
    mypokemon=input('Pikachu or Squirtle')
    random.shuffle(wild_pokemon)
    if mypokemon == 'Pikachu':
        if wild_pokemon[0] == 'Pikachu':
            battle(Pikachu(20), Pikachu(20))
        elif wild_pokemon[0] =='Squirtle':
            battle(Pikachu(20), Squirtle(21))
go_pikachu()
    