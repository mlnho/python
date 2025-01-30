#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9506                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9506                           #+#        #+#      #+#     #
#    Solved: 2024/09/19 21:11:41 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


while True:
    n = int(input())
    if n == -1:
        break

    sum = 0
    list = []
    for i in range(1, n):
        if n % i == 0:
            list.append(i)
            sum += i


    answer = ""

    if sum == n:
        answer += str(n) + " = 1"
        for i in range(2, n):
            if n % i == 0:
                answer += " + " + str(i)
        print(answer)
    else :
        print(str(n) + " is NOT perfect.")