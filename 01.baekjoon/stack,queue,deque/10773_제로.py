# 첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)

# 이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.

# 정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

# 4,3,0,4,0 = 0

# import sys # 시간초과에 대한 sys 추가

k = int(input())

# 스택 선언
numbers = []

for i in range(k):
    number = int(input())
    if number != 0:
        numbers.append(number)
        # print("현재 리스트 상황 : ", numbers)
    else:
        numbers.pop()
        # print("삭제된 후 : ", numbers)

sum = 0
for i in range(len(numbers)):
    sum += numbers[i]

print (sum)