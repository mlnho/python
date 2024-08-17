import sys

N = int(sys.stdin.readline())

for i in range(N):
    input = sys.stdin.readline().strip()
    print(input[0],input[len(input)-1],sep="")
