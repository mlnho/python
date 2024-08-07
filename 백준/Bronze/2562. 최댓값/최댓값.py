import sys

read = sys.stdin.readline

X = []

for i in range(9):
    X.append(int(read()))

print(max(X))
print(X.index(max(X))+1)
