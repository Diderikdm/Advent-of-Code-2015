import itertools 
with open("C:\\Advent\\2015\\day15.txt", 'r') as file:
    ingredients = {x[0]: {y.split(' ')[0] : int(y.split(' ')[1]) for y in x[1].split(', ')} for x in [z.split(': ') for z in file.read().splitlines()]}
    possibles = [[x for x in range(1,100)] for y in range(len(ingredients.keys()))]
    combinations = [x for x in itertools.product(*possibles) if sum(x) == 100]
    values = set()
    cal_values = set()
    a, b, c, d = [x for x in ingredients.keys()]
    for w, x, y, z in combinations:
        cap = sum([ingredients[a]['capacity'] * w, ingredients[b]['capacity'] * x, ingredients[c]['capacity'] * y, ingredients[d]['capacity'] * z])
        dur = sum([ingredients[a]['durability'] * w, ingredients[b]['durability'] * x, ingredients[c]['durability'] * y, ingredients[d]['durability'] * z])
        fla = sum([ingredients[a]['flavor'] * w, ingredients[b]['flavor'] * x, ingredients[c]['flavor'] * y, ingredients[d]['flavor'] * z])
        tex = sum([ingredients[a]['texture'] * w, ingredients[b]['texture'] * x, ingredients[c]['texture'] * y, ingredients[d]['texture'] * z])

        if any(i < 0 for i in [cap, dur, fla, tex]):
            values.add(0)
            continue
        values.add(cap*dur*fla*tex)

        if sum([ingredients[a]['calories'] * w, ingredients[b]['calories'] * x, ingredients[c]['calories'] * y, ingredients[d]['calories'] * z]) == 500:
            cal_values.add(cap*dur*fla*tex)

    print(max(values))
    print(max(cal_values))
