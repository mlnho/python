#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2577                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2577                           #+#        #+#      #+#     #
#    Solved: 2024/09/23 21:10:59 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


A = int(input())
B = int(input())
C = int(input())

number = str(A * B * C)
list = []
for i in range(len(number)):
    list.append(int(number[i]))  # 숫자 값으로 리스트에 넣기

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
answer = [0] * 10
# print("answer : ", answer)

for j in range(len(list)):
    for k in range(len(answer)):
        if list[j] == numbers[k]:
            answer[k] += 1


for o in range(len(answer)):
    print(answer[o])
