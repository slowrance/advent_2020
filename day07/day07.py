with open('input.txt') as f:
    real_input = [line for line in f.readlines()]

test_input = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''.splitlines()

test_input_2 = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''.splitlines()


def contains_shiny_gold(outer_bag: dict) -> bool:
    inner_bags = outer_bag.keys()
    if 'shiny gold' in inner_bags:
        return True
    results = []
    for bag in inner_bags:
        results.append(contains_shiny_gold(rules[bag]))
    return any(results)


def number_in_color(color):
    total = 0
    if len(rules[color]) == 0:
        return 0
    for k, v in rules[color].items():
        total += v + (v * number_in_color(k))
    return total


rules = {}
for rule in real_input:
    outer, inner = rule.split('contain')

    outer = outer.replace('bags', '').strip()
    rules[outer] = {}
    inner_bags = inner.split(',')
    for bag in inner_bags:
        bag = bag.strip()
        bag_parts = bag.split()
        if bag_parts[0].isnumeric():
            tag = ' '.join([bag_parts[1], bag_parts[2]])
            rules[outer][tag] = int(bag_parts[0])

print(rules)

results = []
for i, rule in enumerate(rules.items()):
    results.append(contains_shiny_gold(rule[1]))

total = 0
for result in results:
    if result is True:
        total += 1
print(total)

total_bags = 0
total_bags += number_in_color('shiny gold')
print(total_bags)
