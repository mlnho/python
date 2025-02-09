#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 28278                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/28278                          #+#        #+#      #+#     #
#    Solved: 2025/02/09 14:20:25 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

def stack(N):
    stack = []
    for i in range(N):
        num = list(map(int, sys.stdin.readline().split()))
        if num[0]== 1:
            stack.append(num[1])
        elif num[0] == 2:
            # if len(stack) > 0:
            if stack: # true 의미
                print(stack.pop())
            else :
                print(-1)
        elif num[0] == 3:
            print(len(stack))
        elif num[0] == 4:
            # if len(stack) > 0:
            if stack:
                print(0)
            else:
                print(1)
        else:
            if stack:
                print(stack[-1])
            else:
                print(-1)


# print(stack(int(input()))) # None 이 출력된다.
stack(int(sys.stdin.readline()))