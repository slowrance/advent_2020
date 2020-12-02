with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

total = 0
for line in lines:
    parts = line.split()
    nums = parts[0].split('-')
    low_num = int(nums[0])
    high_num = int(nums[1])
    letter = parts[1][0]
    password = parts[2]
    count = 0
    for char in password:
        if char == letter:
            count += 1
    if count >= low_num and count <= high_num:
        total += 1
    # print(low_num, high_num, letter, password)

print(total)


total = 0
for line in lines:
    parts = line.split()
    nums = parts[0].split('-')
    low_num = int(nums[0])
    high_num = int(nums[1])
    letter = parts[1][0]
    password = parts[2]
    if password[low_num - 1] == letter and password[high_num - 1] == letter:
        pass
    elif password[low_num - 1] == letter or password[high_num - 1] == letter:
        total +=1

print(total)

