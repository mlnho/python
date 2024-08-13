import sys

N, M = map(int, sys.stdin.readline().split())

basket = [i for i in range(1, N + 1)]

for f in range(M):
    i, j = map(int, sys.stdin.readline().split())
    tmp = basket[i - 1:j]
    tmp.reverse()
    basket[i - 1:j] = tmp

print(*basket)
