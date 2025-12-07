import sys

input = open(sys.argv[1]).read().rstrip()
lines = input.split("\n")

result = 0
battery_size = 12
for bank in lines:
    battery = []
    curr_pos = 0
    for offset in reversed(range(battery_size)):
        curr_max = 0
        valid_numbers = bank[curr_pos : len(bank) - offset]
        max_pos = 0
        for i in range(len(valid_numbers)):
            contender = int(valid_numbers[i])
            if contender > curr_max:
                curr_max = contender
                max_pos = i
        curr_pos += max_pos + 1
        battery.append(str(curr_max))
    result += int("".join(battery))

print(result)
