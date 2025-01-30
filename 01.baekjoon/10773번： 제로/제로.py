#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10773                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10773                          #+#        #+#      #+#     #
#    Solved: 2024/10/01 12:02:33 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

K = int(sys.stdin.readline())

stack = []

for i in range(K):
    order = int(sys.stdin.readline())
    if order == 0:
        stack.pop()
    else:
        stack.append(order)

sum = 0
for i in stack:
    sum += i

print(sum)