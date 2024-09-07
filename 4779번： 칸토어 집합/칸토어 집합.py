#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4779                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4779                           #+#        #+#      #+#     #
#    Solved: 2024/09/07 18:19:53 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


## 풀이 1 : bottom up 방식

# ans = ["" for _ in range(13)]

# ans[0] = "-"

# for i in range(1, 13):
#     ans[i] = ans[i - 1] + (" " * (3 ** (i - 1))) + ans[i - 1]

# while True:
#     try:
#         N = int(input())
#         print(ans[N])
#     except:
#         break


## 풀이 2 : 재귀함수

def fibo(x):
    # base case 
    if x == 0:
        return "-"
    
    # recursive case
    return fibo(x-1) + (" " * (3 ** (x-1))) + fibo(x-1)


while True:
    try:
        N = int(input())
        print(fibo(N))
    except:
        break