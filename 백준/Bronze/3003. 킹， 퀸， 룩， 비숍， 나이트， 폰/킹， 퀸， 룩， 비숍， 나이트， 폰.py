import sys

user = list(map(int, sys.stdin.readline().split()))

chess = [1, 1, 2, 2, 2, 8]

answer = []

for i in range(len(user)):
    number = chess[i] - user[i]
    answer.append(number)

print(*answer)
