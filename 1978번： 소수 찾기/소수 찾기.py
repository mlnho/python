#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1978                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1978                           #+#        #+#      #+#     #
#    Solved: 2024/09/20 20:19:43 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


N = int(input())

answer = 0

numbers = list(map(int,input().split()))

for i in range(len(numbers)):
    number = numbers[i]
    for j in range(2,number+1): # 소수 찾기에 0과 1은 제외
        if number == j: # 반복문이 끝까지 갔다는 소리 따라서 소수
            answer += 1
        elif number % j == 0: # 만약 반복문이 해당 수까지 가는 과정에서 나눠진다면 소수가 X
            break
    

print(answer)
            
            