#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10974                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10974                          #+#        #+#      #+#     #
#    Solved: 2024/09/25 22:28:11 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


def permutation(level):
    global N, choose, check
    # base case
    if level == N:
        print(*choose)
        return

    # recursive case
    for i in range(1, N + 1):
        if check[i] == True:
            continue
        
        choose.append(i)    
        check[i] = True
        permutation(level + 1)
        check[i] = False
        choose.pop()


N = int(input())
choose = []  # 최종 결과 값
check = [False] * (N + 1)

permutation(0)
