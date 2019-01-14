import random

class Pokemon:
    species = '포켓몬'
    type_weight = {
        'normal': { 'strong': [], 'weak': ['rock', 'ghost'] },
        'elec': { 'strong': ['water', 'flying'], 'weak': ['ground', 'elec'] },
        'water': { 'strong': ['fire', 'ground', 'rock'], 'weak': ['water'] },
        'rock': { 'strong': ['fire', 'ice'], 'weak': ['ground'] },
        'ground': { 'strong': ['fire', 'elec', 'rock', 'poison'], 'weak': [] },
        'ice': { 'strong': ['ground'], 'weak': ['fire', 'water', 'ice'] },
        'fire': { 'strong': ['ice'], 'weak': ['fire', 'water', 'rock'] },
        'poison': { 'strong': [], 'weak': ['poison', 'rock', 'ground'] }
    }
    abnormal_conditions = ['poison', 'burn', 'freeze', 'paralysis']
    
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = level * 10
        
    def set_hp(self, point):
        self.hp += point
        
    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level
    
    def get_hp(self):
        return self.hp
    
    def get_speed(self):
        return self.pokemon_stats['speed'] * self.get_level()
        
    def check_status(self):
        if self.hp > 0:
            return True
        else:
            return False
        
    def check_actionable(self):
        return self.pokemon_stats['actionable']
    
    def change_actionable(self, value):
        self.pokemon_stats['actionable'] = value
        
    def get_type_weight(self, skill_type, enemy):
        weight = 1.5
        strong_type = self.type_weight[skill_type]['strong']
        weak_type = self.type_weight[skill_type]['weak']
        for enemy_type in enemy.pokemon_stats['pokemon_type']:
            if enemy_type in strong_type:
                weight *= 2
            if enemy_type in weak_type:
                weight /= 2
        return weight
    
    def get_info(self):
        return f'{self.get_name()}(lv{self.get_level()}, {self.species})' 
        
    def affect_abnormal_condition(self):
        actionable = True
        for condition, turn in self.pokemon_stats['condition'].items():
            if condition == 'poison':
                self.affect_poison(turn)
            if condition == 'burn':
                self.affect_burn(turn)
            if condition == 'freeze':
                actionable = actionable and self.affect_freeze(turn)
            if condition == 'paralysis':
                actionable = actionable and self.affect_paralysis(turn)
        self.change_actionable(actionable)
                  
    def affect_poison(self, turn):
        if turn > 0:
            self.pokemon_stats['condition']['poison'] -= 1
            dmg = int(-1 * self.get_level() * 10 / 16)
            self.set_hp(dmg)
            print(f'{self.get_info()}은(는) 독에 중독되어 피해를 {-dmg} 입었다.')
              
    def affect_burn(self, turn):
        if turn > 0:
            self.pokemon_stats['condition']['burn'] -= 1
            dmg = int(-1 * self.get_level() * 10 / 16)
            self.set_hp(dmg)
            print(f'{self.get_info()}은(는) 화상 피해를 {-dmg} 입었다.')    
              
    def affect_freeze(self, turn):
        if turn > 0:
            self.pokemon_stats['condition']['freeze'] -= 1
            print(f'{self.get_info()}은(는) 얼어서 움직일 수 없다!')
            return False
        else:
            self.change_actionable(True)
            return True
    
    def affect_paralysis(self, turn):
        if turn > 0:
            self.pokemon_stats['condition']['paralysis'] -= 1
            print(f'{self.get_info()}은(는) 마비되어 움직일 수 없다!')   
            return False
        else:
            return True
        
    def add_abnormal_conditions(self, enemy, skill_type):
        if skill_type == 'fire':
            if random.choice(range(100)) < 60:
                enemy.pokemon_stats['condition']['burn'] = 2
                print(f'{enemy.get_info()}은(는) 화상을 입었다.')
        if skill_type == 'ice':
            if random.choice(range(100)) < 30:
                enemy.pokemon_stats['condition']['freeze'] = 1
                print(f'{enemy.get_info()}은(는) 얼었다.')
        if skill_type == 'elec':
            if random.choice(range(100)) < 30:
                enemy.pokemon_stats['condition']['paralysis'] = 1  
                print(f'{enemy.get_info()}은(는) 마비됐다.')
        if skill_type == 'poison':
            if random.choice(range(100)) < 60:
                enemy.pokemon_stats['condition']['poison'] = 2
                print(f'{enemy.get_info()}은(는) 중독됐다.')
        
    def attack(self, enemy):
        skill = random.choice(self.skill_list)
        weight = self.get_type_weight(skill['type'], enemy)
        dmg = int(-1 * skill['ap'] * self.level * weight)
        enemy.set_hp(dmg)
        print(f'{self.get_info()}의 {skill["name"]} 공격')
        if weight > 1.5:
            print('효과는 굉장했다!')
        elif weight < 1.5:
            print('효과는 미미했다.')
        print(f'{enemy.get_info()}에게 피해를 {-dmg} 입혔다!')
        self.add_abnormal_conditions(enemy, skill['type'])
        print('-  -  -  -  -  -  -  -  -  -  -  -  -  -')

              
              
class Pikachu(Pokemon):
    species = '피카츄'
    pokemon_stats = { 'actionable': True, 'pokemon_type': ['elec'], 'speed': 1.5, 'condition': {} }
    skill_list = [
        { 'name': '몸통 박치기', 'ap': 1, 'type': 'normal' },
        { 'name': '10만 볼트', 'ap': 1.2, 'type': 'elec' },
        { 'name': '전광석화', 'ap': 1.2, 'type': 'normal' },
        { 'name': '번개', 'ap': 1.4, 'type': 'elec' }
    ]


class Squirtle(Pokemon):
    species = '꼬부기'
    pokemon_stats = { 'actionable': True, 'pokemon_type': ['water'], 'speed': 1.2, 'condition': {} }
    skill_list = [
        { 'name': '몸통 박치기', 'ap': 1, 'type': 'normal' },
        { 'name': '물대포', 'ap': 1.1, 'type': 'water' },
        { 'name': '하이드로펌프', 'ap': 1.4, 'type': 'water' },
        { 'name': '냉동 펀치', 'ap': 1.3, 'type': 'ice' }
    ]
              
              
class Onix(Pokemon):
    species = '롱스톤'
    pokemon_stats = { 'actionable': True, 'pokemon_type': ['rock', 'ground'], 'speed': 0.9, 'condition': {} }
    skill_list = [
        { 'name': '몸통 박치기', 'ap': 1, 'type': 'normal' },
        { 'name': '돌떨구기', 'ap': 1.1, 'type': 'rock' },
        { 'name': '모래지옥', 'ap': 0.8, 'type': 'ground' },
        { 'name': '스톤에지', 'ap': 1.3, 'type': 'rock' }
    ]              
           
              
class Charmander(Pokemon):
    species = '파이리'
    pokemon_stats = { 'actionable': True, 'pokemon_type': ['fire'], 'speed': 1.2, 'condition': {} }
    skill_list = [
        { 'name': '할퀴기', 'ap': 1, 'type': 'normal' },
        { 'name': '불꽃세례', 'ap': 1.1, 'type': 'fire' },
        { 'name': '화염방사', 'ap': 1.3, 'type': 'fire' },
        { 'name': '불꽃엄니', 'ap': 1.2, 'type': 'fire' }
    ] 
          
              
class Arbok(Pokemon):
    species = '아보크'
    pokemon_stats = { 'actionable': True, 'pokemon_type': ['poison'], 'speed': 1.3, 'condition': {} }
    skill_list = [
        { 'name': '몸통 박치기', 'ap': 1, 'type': 'normal' },
        { 'name': '독침', 'ap': 0.8, 'type': 'poison' },
        { 'name': '용해액', 'ap': 0.9, 'type': 'poison' },
        { 'name': '더스트슈트', 'ap': 1.4, 'type': 'poison' }
    ]               
              
        
def battle(p1, p2):
    p_list = [p1, p2]
    if p1.get_speed() > p2.get_speed():
        p_list = [p1, p2]
    elif p1.get_speed() < p2.get_speed():
        p_list = [p2, p1]
    else:
        random.shuffle(p_list)
    
    p_list[0].affect_abnormal_condition()
    if p_list[0].check_status() and p_list[0].check_actionable():
        p_list[0].attack(p_list[1])
        print(f'{p1.get_info()}의 체력 : {p1.get_hp()}\n{p2.get_info()}의 체력 : {p2.get_hp()}')
        print('-----------------------------------------')

    if p_list[1].check_status():
        p_list[1].affect_abnormal_condition()
    if p_list[1].check_status() and p_list[1].check_actionable():
        p_list[1].attack(p_list[0])
        print(f'{p1.get_info()}의 체력 : {p1.get_hp()}\n{p2.get_info()}의 체력 : {p2.get_hp()}')
        print('-----------------------------------------')
        
              
class PokemonCreater:
    pokemon_list = ['Pikachu', 'Squirtle', 'Onix', 'Charmander', 'Arbok']
              
    def create_pokemon(self, species, nickname):
        level = random.choice(range(5, 15))
        if species == 'Pikachu':
              return Pikachu(nickname, level)
        elif species == 'Squirtle':
              return Squirtle(nickname, level)
        elif species == 'Onix':
              return Onix(nickname, level)
        elif species == 'Charmander':
              return Charmander(nickname, level)
        elif species == 'Arbok':
              return Arbok(nickname, level)
        else:
              return None
            
    def create_random_pokemon(self, nickname):
        species = random.choice(self.pokemon_list)
        return self.create_pokemon(species, nickname)
        
              
        
        
        
        
creater = PokemonCreater()
p1 = creater.create_random_pokemon('A')
p2 = creater.create_random_pokemon('B')

print('+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+\n')
print(f'{p1.get_info()} vs {p2.get_info()}')
print('\n+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+')

while p1.check_status() and p2.check_status():
    battle(p1, p2)
print()
if not p1.check_status():    
    print(f'{p2.get_info()} win')
    print(f'{p1.get_info()} lose')
else:
    print(f'{p1.get_info()} win')
    print(f'{p2.get_info()} lose')
print('\n-----------------------------------------')