import sys

read = sys.stdin.readline

T = int(read())

for i in range(1, T + 1):
    for j in range(T - i):
        print(" ", end="")
    for p in range(i):
        print("*", end="")
    print("")
