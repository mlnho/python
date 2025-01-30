#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10828                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10828                          #+#        #+#      #+#     #
#    Solved: 2024/10/01 11:28:42 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys  # 시간초과가 났어서 sys로 수정

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    lst = list(sys.stdin.readline().split())  # 입력 값 받기
    if "push" in lst:
        stack.append(lst[1])
        # print('현재 stack :',stack)
    elif "pop" in lst:
        if len(stack) == 0:  # stack 이 빈 리스트일 경우에
            print(-1)
        else:
            print(stack.pop())
    elif "size" in lst:
        print(len(stack))
    elif "empty" in lst:
        if len(stack) == 0:  # stack 이 빈 리스트일 경우에
            print(1)
        else:
            print(0)
    elif "top" in lst:
        if len(stack) == 0:  # stack 이 빈 리스트일 경우에
            print(-1)
        else:
            print(stack[-1])
