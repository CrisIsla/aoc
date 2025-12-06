import sys

input_ = open(sys.argv[1]).read().rstrip()
ranges = input_.split(",")


def getDivisors(n):
    divisors = []
    if n == 1:
        return [1]
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def getInvalids(l, r):
    digitsl = len(str(l))
    digitsr = len(str(r))
    invalids = []
    if digitsl < digitsr:
        invalids += getInvalids(10**digitsl, r)
        r = (10**digitsl) - 1
    divisors = getDivisors(digitsl)
    for n in divisors:
        repetitions = digitsl // n
        values = []
        min = int(str(l)[:n])
        max = int(str(r)[:n])
        possible_patterns = [min] if min == max else range(min, max + 1)
        for pattern in possible_patterns:
            number = 0
            for i in range(repetitions):
                number += pattern * (10 ** (i * n))
            if l <= number and number <= r:
                values.append(number)

        invalids += values
    return invalids


result = 0
result2 = 0
invalids = []
for interval in ranges:
    l, r = interval.split("-")
    values = getInvalids(int(l), int(r))
    invalids += values
    for i in range(int(l), int(r) + 1):
        number = str(i)
        length = len(number)
        if length % 2 == 0:
            nr = number[length // 2 :]
            if number[: length // 2] == nr:
                result += i

print(result)
print(sum({x for x in set(invalids) if x > 9}))
