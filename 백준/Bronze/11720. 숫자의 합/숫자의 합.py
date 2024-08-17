import sys

N = int(sys.stdin.readline())

number = list(map(int, sys.stdin.readline().rstrip()))

sum = 0
for i in range(len(number)):
    sum += number[i]

print(sum)
