#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3273                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3273                           #+#        #+#      #+#     #
#    Solved: 2024/09/24 22:21:20 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# 투포인터로 풀어야 시간초과 안남,,
import sys

n = int(sys.stdin.readline())

num_list = sorted(list(map(int, sys.stdin.readline().split())))  # 순서대로 정렬

x = int(sys.stdin.readline())

answer = 0
left, right = 0, n - 1

while left < right:
    num = num_list[left] + num_list[right]
    if num == x:
        answer += 1
        left += 1
    elif num < x:
        left += 1
    elif num > x:
        right -= 1

print(answer)
