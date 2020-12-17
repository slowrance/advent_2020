import copy
from collections import defaultdict

with open('input.txt') as f:
    raw = f.read()
    real_input = raw.split('\n\n')

test_input = '''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''.split('\n\n')


used_input = real_input

fields, my_ticket, near_tickets = used_input

def get_field_values(fields: str):
    values = set()
    field_rules = defaultdict(set)
    fields = fields.split('\n')
    for field in fields:
        field_name, rules = field.split(': ')
        numbers = rules.split(' or ')
        for num in numbers:
            num1, num2 = num.split('-')
            nums = range(int(num1), int(num2) + 1)
            for num in nums:
                values.add(num)
                field_rules[field_name].add(num)
    return values, field_rules

def get_valid_tickets(near_tickets: str, valid_values: set) -> list:
    valid_tickets = []
    tickets = near_tickets.split('\n')
    for ticket in tickets[1:]:
        nums = ticket.split(',')
        if all([int(num) in valid_values for num in nums]):
            valid_tickets.append([int(num) for num in nums])
    return valid_tickets

fields_nums, field_rules = get_field_values(fields)
valid_tickets = get_valid_tickets(near_tickets, fields_nums)
print(valid_tickets)

def possible_fields(valid_tickets):
    all_possibles = []
    for ticket in valid_tickets:
        possibles = defaultdict(set)
        for i, num in enumerate(ticket):
            for k, v in field_rules.items():
                if num in v:
                    possibles[i].add(k)
        all_possibles.append(possibles)
    return all_possibles

all_possibles = possible_fields(valid_tickets)
field_list = {}
field_names = field_rules.keys()
for i in range(len(valid_tickets)):
    field_list[i] = set(field_names)
for possible in all_possibles:
    for k, v in possible.items():
        field_list[k] = field_list[k].intersection(possible[k])
print(field_list)

available_fields = set(field_names)
print(available_fields)

field_labels = {i: '' for i in range(len(field_names))}

def get_field_labels(available_fields, field_list):
    if len(field_list) == 0:
        return None
    if len(field_list) == 1:
        return {}

    for k, v in available_fields.items():
        # if len(available_fields[k]) == 1 and v.pop() in field_labels:
        #     continue
        new_available_fields = copy.deepcopy(available_fields)
        # v = v.intersection(field_list)
        for i in v:

            # new_field_list = v.intersection(field_list)
            s = set()
            s.add(i)
            # available_fields[k] = s
            new_field_list = copy.deepcopy(field_list)
            # new_field_list.discard(i)
            new_available_fields[k] = s
            result = get_field_labels(new_available_fields, new_field_list)

            if result is not None:
                field_labels[k] = i
                field_list.discard(i)
                return field_labels

        # return available_fields
    return field_labels

# def get_field_labels(field_list, available_fields):
#     new_field_list = copy.copy(field_list)
#     if len(available_fields) == 0:
#         return field_labels
#     for k, v in field_list.items():
#         if len(v) == 1:
#             field_labels[k] = v.pop()
#             available_fields.discard(v)
#             del new_field_list[k]
#         if len(v) > 1:
#             new_field_list[k] = v.intersection(available_fields)
#     if '' in field_labels.values():
#         get_field_labels(new_field_list, available_fields)
#
#
#     return field_labels

print(get_field_labels(field_list, available_fields))
