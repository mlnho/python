#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10870                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10870                          #+#        #+#      #+#     #
#    Solved: 2024/09/07 17:28:13 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 풀이 1
# 반복문 + 메모이제이션

# n = int(input())

# arr = [-1] * (n+2)
# arr[0]=0
# arr[1]=1

# for i in range(2, n+1):
#     arr[i] = arr[i-1] + arr[i-2]

# print(arr[n])


# 재귀함수
def fibo(n):
    # base case
    if n == 0:
        return 0
    if n == 1:
        return 1

    # recursive case
    return fibo(n - 1) + fibo(n - 2)


n = int(input())

print(fibo(n))
