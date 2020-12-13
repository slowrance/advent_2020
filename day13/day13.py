import math

with open('input.txt') as f:
    real_input = [line.strip() for line in f]

test_input = '''939
7,13,x,x,59,x,31,19'''.splitlines()

used_input = real_input

earliest, times = used_input
earliest = int(earliest)
times = times.split(',')
buses = [(time_after, int(bus)) for time_after, bus in enumerate(times) if bus.isnumeric()]
times = [int(time) for time in times if time.isnumeric()]

print(earliest, times)
min_time = 1000
for time in times:
    current_time = math.ceil(earliest / time) * time - earliest
    if current_time < min_time:
        min_time = current_time
        print(time, min_time, time * min_time)



# part 2
offsets = [(time_after % bus, bus) for time_after, bus in buses]
candidate, increment = 0, 1
for time_after, bus in offsets:
  while candidate % bus != (bus-time_after if time_after > 0 else 0):
    candidate += increment
  increment *= bus
print(candidate)
