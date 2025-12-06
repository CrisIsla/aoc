import sys

input = open(sys.argv[1]).read().rstrip()
ranges = input.split(",")

result = 0
for interval in ranges:
    l, r = interval.split("-")
    for i in range(int(l), int(r) + 1):
        number = str(i)
        length = len(number)
        if length % 2 == 0:
            nr = number[length // 2 :]
            if number[: length // 2] == nr:
                result += i

print(result)
