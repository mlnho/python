import sys

read = sys.stdin.readline

N = int(read())

X = list(map(int, read().split()))

print(min(X), max(X))
