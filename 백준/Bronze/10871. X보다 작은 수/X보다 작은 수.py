import sys

read = sys.stdin.readline

N, X = map(int, read().split())

# 숫자 리스트
A = list(map(int, read().split()))

answer = []

for i in A:
    if i < X:
        answer.append(i)

# 출력 값
for i in answer:
    print(i, end=" ")
