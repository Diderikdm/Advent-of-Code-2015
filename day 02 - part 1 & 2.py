import itertools
import functools

def calculate_ribbon_needed(box):
    dimensions = [int(x) for x in box.split('x')]
    ribbon = sum([2*x for x in sorted(dimensions)[:2]]) + functools.reduce(lambda x,y: x*y, dimensions)
    return ribbon

def calculate_wrapping_paper_needed(box):
    dimensions = [int(x) for x in box.split('x')]
    combinations = list(itertools.combinations(dimensions, 2))
    raw_packing = [2*x*y for x,y in combinations]
    packing = sum(raw_packing) + min(raw_packing)//2
    return packing

with open('C:\\Users\\dider\\AppData\\Local\\Programs\\Python\\Python39\\AoC 2015\\input\\day2.txt', 'r') as file:
    data = file.read().splitlines()
    print('Part 1: {}'.format(sum([calculate_wrapping_paper_needed(box) for box in data])))
    print('Part 2: {}'.format(sum([calculate_ribbon_needed(box) for box in data])))
