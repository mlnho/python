#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2563                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2563                           #+#        #+#      #+#     #
#    Solved: 2024/09/18 20:36:19 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 정사각형 도화지 가로세로 100
array = [[0]*100 for _ in range(100)]

# print(array)

answer = 0

for i in range(int(input())): # 색종의 수 
    lef,bot = map(int,input().split())
    for j in range(lef,lef+10):
        for z in range(bot,bot+10):
            if array[j][z] != 1:
                array[j][z] += 1
                answer += 1

print(answer)
                