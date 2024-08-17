import sys

T = int(sys.stdin.readline().rstrip())

answer = ""

for i in range(T):
    num, word = sys.stdin.readline().rstrip().split()
    for j in range(len(word)):
        answer += int(num) * word[j]

    print(answer)
    answer = ""

