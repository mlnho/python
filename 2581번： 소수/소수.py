#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2581                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2581                           #+#        #+#      #+#     #
#    Solved: 2024/09/20 21:11:27 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# M이상 N이하 자연수 중 소수 
M = int(input())
N = int(input())

num_list = []
# 최대값
sum = 0
# 최소값
min = 0

for i in range(M,N+1):
    for j in range(2,i+1):
        if j == i:
            num_list.append(i)
            sum += i
        elif i % j == 0:
            break

# print(num_list)s

if not num_list:
    print(-1)
else:
    print(sum)
    print(num_list[0])
