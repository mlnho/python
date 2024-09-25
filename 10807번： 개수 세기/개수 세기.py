#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10807                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10807                          #+#        #+#      #+#     #
#    Solved: 2024/09/25 22:56:22 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


N = int(input())

numbers = list(map(int, input().split()))
v = int(input())

answer = 0
for i in numbers:
    if i == v:
        answer += 1
        
print(answer)