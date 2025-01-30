#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2566                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2566                           #+#        #+#      #+#     #
#    Solved: 2024/09/10 21:35:59 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


array = []

# 9 x 9 만들기
for _ in range(9):
    row = list(map(int, input().split()))
    array.append(row)


max_num = 0
row_num = 0
col_num = 0

for i in range(9):
    for j in range(9):
        if array[i][j] >= max_num:
            max_num = array[i][j]
            row_num = i+1
            col_num = j+1

print(max_num)
print(row_num,col_num)
