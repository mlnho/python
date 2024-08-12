import sys

read = sys.stdin.readline

answer = []

for i in range(10):
    A = int(read())
    answer.append(A % 42)

answer = set(answer)

print(len(answer))
