def fight(spells, cooldowns, boss_hp, boss_dmg, hp=50, mana=500, mana_spent=0, chain=[], default = 0):

    for spell, stats in spells.items():
     
        temp_boss_hp = boss_hp
        temp_hp = hp
        temp_mana = mana
        temp_mana_spent = mana_spent
        armor = 0
        temp_cooldowns = {k:v for k,v in cooldowns.items()}
        temp_skip = []
        temp_chain = []

        temp_hp -= default

        if temp_hp < 1:
            continue

        temp_boss_hp -= sum(spells[x]['Damage'] for x in temp_cooldowns if x not in temp_skip)
        armor = sum(spells[x]['Armor'] for x in temp_cooldowns if x not in temp_skip)
        temp_mana += sum(spells[x]['Recharge'] for x in temp_cooldowns if x not in temp_skip)

        for k,v in temp_cooldowns.items():
            if k not in temp_skip:
                temp_cooldowns[k] -= 1

        to_remove = [k for k in temp_cooldowns.keys() if temp_cooldowns[k] == 0]

        for k in to_remove:
            temp_cooldowns.pop(k)

        if spell not in ['Magic Missile', 'Drain']:
            if spell not in temp_cooldowns:
                temp_cooldowns[spell] = stats['Time']
                temp_skip.append(spell)
            else:
                continue
            
        if temp_boss_hp < 1:
            if temp_mana_spent not in win_costs:
                win_costs.append((temp_mana_spent, temp_chain))
            continue

        if stats['Cost'] > temp_mana:
            continue
              
        damage = stats['Damage'] if stats['Time'] == 1 else 0
        heal = stats['Heal']

        temp_boss_hp -= damage
        temp_hp += heal

        temp_mana -= stats['Cost']

        temp_mana_spent += stats['Cost']
   
        temp_chain = [x for x in chain] + [spell]
        
        temp_boss_hp -= sum(spells[x]['Damage'] for x in temp_cooldowns)
        armor = sum(spells[x]['Armor'] for x in temp_cooldowns)
        temp_mana += sum(spells[x]['Recharge'] for x in temp_cooldowns)
        
        if temp_boss_hp < 1:
            if temp_mana_spent not in win_costs:
                win_costs.append((temp_mana_spent, temp_chain))
            continue
            
        for k,v in temp_cooldowns.items():
            temp_cooldowns[k] -= 1

        to_remove = [k for k in temp_cooldowns.keys() if temp_cooldowns[k] == 0]

        for k in to_remove:
            temp_cooldowns.pop(k)
        
        temp_hp -= max(boss_dmg - armor, 1)

        if temp_hp < 1:
            continue
        
        fight(spells, {k:v for k,v in temp_cooldowns.items()}, temp_boss_hp, boss_dmg, temp_hp, temp_mana, temp_mana_spent, temp_chain, default)

    return


def build_spells(data, build_magic = lambda u,v,w,x,y,z: {'Cost' : int(u), 'Damage' : int(v), 'Armor' : int(w), 'Time' : int(x), 'Recharge' : int(y), 'Heal' : int(z)}):
    return {x[0] : build_magic(*x[1:]) for x in data}                                                                                                                                                                                                 

    
with open("C:\\Advent\\2015\\day22.txt", 'r') as file:
    data = {x.split(': ')[0] : int(x.split(': ')[1]) for x in file.read().splitlines()}

    spells = build_spells(reversed([
        ["Magic Missile", 53, 4, 0, 1, 0, 0],
        ["Drain", 73, 2, 0, 1, 0, 2],
        ["Shield", 113, 0, 7, 6, 0, 0],
        ["Poison", 173, 3, 0, 6, 0, 0],
        ["Recharge", 229, 0, 0, 5, 101, 0]
        ]))

    win_costs = []
    
    fight(spells, {}, data['Hit Points'], data['Damage'])

    print(min([x[0] for x in win_costs]))

    win_costs = []

    fight(spells, {}, data['Hit Points'], data['Damage'], default=1)

    print(min([x[0] for x in win_costs]))
   
