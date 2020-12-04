import re

test_input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

with open('input.txt') as f:
    real_input = f.read()

passports = real_input.split('\n\n')
passport_list = []
for passport in passports:
    fields = ' '.join(passport.splitlines()).split()
    passport_dict = {}
    for field in fields:
        key, val = field.split(':')
        passport_dict[key] = val
    passport_list.append(passport_dict)

# part 1
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_count = 0
for passport in passport_list:
    if all(field in passport.keys() for field in required_fields):
        valid_count += 1

print(valid_count)


# part 2
def valid_byr(value):
    if value is not None and value.isnumeric() and 1920 <= int(value) <= 2002 and len(value) == 4:
        return True
    return False


def valid_iyr(value):
    if value is not None and value.isnumeric() and 2010 <= int(value) <= 2020 and len(value) == 4:
        return True
    return False


def valid_eyr(value):
    if value is not None and value.isnumeric() and 2020 <= int(value) <= 2030 and len(value) == 4:
        return True
    return False


def valid_hgt(value):
    if value is not None:
        if value[-2:] == 'cm':
            if value[:-2].isnumeric() and 150 <= int(value[:-2]) <= 193:
                return True
        if value[-2:] == 'in':
            if value[:-2].isnumeric() and 59 <= int(value[:-2]) <= 76:
                return True
    return False


def valid_hcl(value):
    if value:
        return re.match(r'#[0-9a-f]{6}', value)
    return False


def valid_ecl(value):
    if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False


def valid_pid(value):
    if value is not None and value.isnumeric() and len(value) == 9:
        return True
    return False


required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_count = 0
for passport in passport_list:
    byr = passport.get('byr')
    iyr = passport.get('iyr')
    eyr = passport.get('eyr')
    hgt = passport.get('hgt')
    hcl = passport.get('hcl')
    ecl = passport.get('ecl')
    pid = passport.get('pid')
    if all([valid_byr(byr), valid_iyr(iyr), valid_eyr(eyr), valid_hgt(hgt), valid_hcl(hcl), valid_ecl(ecl), valid_pid(pid)]):
        valid_count += 1
print(valid_count)
