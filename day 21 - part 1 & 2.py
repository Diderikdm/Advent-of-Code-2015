from itertools import combinations

def fight(attributes, boss_hitpoints, boss_damage, boss_armor, hit_points=100):
    damage = sum(total[x]['Damage'] for x in attributes)
    armor = sum(total[x]['Armor'] for x in attributes)
    cost = sum(total[x]['Cost'] for x in attributes)

    i = 1
    while hit_points > 0 and boss_hitpoints > 0:
        if i%2 == 1:
            boss_hitpoints -= max(damage - boss_armor, 1)
        else:
            hit_points -= max(boss_damage - armor, 1)
        i+=1

    if hit_points > 0:
        win_costs.append(cost)
    else:
        lose_costs.append(cost)
        

def build_sets(sets, build=[]):
    for needed, items in sets:
        for x in needed:
            combs = [list(x) if len(x) > 1 else [x[0]] for x in combinations(items.keys(), x) if x]
            if combs:
                for y in combs:
                    build_sets(sets[1:], build + [z for z in y])
            else:
                build_sets(sets[1:], build)
        break
    if not sets:
        builds.append(build)

            
def build_item_class(string, build_equipment = lambda x,y,z: {'Cost' : int(x), 'Damage' : int(y), 'Armor' : int(z)}):
    return {(z[0] if len(z) < 5 else ' '.join(z[:2])) : build_equipment(*(z[1:] if len(z) < 5 else z[2:])) for z in [[y for y in x.split(' ') if y] for x in string.strip('\n').splitlines()]}                                                                                                                                                                                                    

    
with open("C:\\Advent\\2015\\day21.txt", 'r') as file:
    data = {x.split(': ')[0] : int(x.split(': ')[1]) for x in file.read().splitlines()}
    weapons = build_item_class("""
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
""")
    armor = build_item_class("""
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
""")
    rings = build_item_class("""
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
""")
    builds = []
    build_sets([([1], weapons), ([0,1], armor), ([0,1,2], rings)])
    total = dict(dict(weapons, ** armor), **rings)
    win_costs, lose_costs = [], []
    
    for build in builds:
        fight(build, boss_hitpoints = data['Hit Points'], boss_damage = data['Damage'], boss_armor = data['Armor'])
    print(min(win_costs))
    print(max(lose_costs))

    

