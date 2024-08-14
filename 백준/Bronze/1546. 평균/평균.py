import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

M = max(numbers)
sum = 0

for i in range(N):
    numbers[i] = numbers[i] / M * 100
    sum += numbers[i]

print(sum / N)
