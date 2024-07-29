import sys

read = sys.stdin.readline

T = int(read())

# 숫자 리스트
num_list = list(map(int, read().split()))

# 찾아야 되는 수
num = int(read())
count = 0

for i in num_list:
    if i == num:
        count += 1

print(count)
