with open('input.txt') as f:
    raw = f.read()
    real_input = raw.split('\n\n')

test_input = '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''.split('\n\n')

used_input = real_input

fields, my_ticket, near_tickets = used_input

def get_field_values(fields: str) -> set:
    values = set()
    fields = fields.split('\n')
    for field in fields:
        field_name, rules = field.split(': ')
        numbers = rules.split(' or ')
        for num in numbers:
            num1, num2 = num.split('-')
            nums = range(int(num1), int(num2) + 1)
            for num in nums:
                values.add(num)
    return values

def get_near_tickets(near_tickets: str) -> list:
    values = []
    tickets = near_tickets.split('\n')
    for ticket in tickets[1:]:
        nums = ticket.split(',')
        for num in nums:
            values.append(int(num))
    return values

fields_nums = get_field_values(fields)
near_ticket_nums = get_near_tickets(near_tickets)
diff = sum([num for num in near_ticket_nums if num not in fields_nums])
print(diff)
