#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2738                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2738                           #+#        #+#      #+#     #
#    Solved: 2024/09/08 16:53:27 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 행 : N
# 열 : M
N, M = map(int, input().split())


# 파이썬 2차원 배열 선언 및 초기화 with for문
arr1 = [[-1 for i in range(M)] for _ in range(N)]


for i in range(len(arr1)):
    num = list(map(int, input().split()))
    for j in range(len(arr1[i])):
        arr1[i][j] = num[j]

for v in range(len(arr1)):
    num = list(map(int, input().split()))
    for x in range(len(arr1[v])):
        arr1[v][x] += num[x]

for p in range(len(arr1)):
    for q in range(len(arr1[p])):
        print(arr1[p][q], end=" ")
    print()