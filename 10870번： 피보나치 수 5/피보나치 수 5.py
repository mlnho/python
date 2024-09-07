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
# def fibo(n):
#     # base case
#     if n == 0:
#         return 0

#     # recursive case
#     return fibo(n - 1) + fibo(n - 2)


# n = int(input())

# print(fibo(n))

# 재귀함수 + 메모이제이션
# 메모이제이션 : 똑같은 수를 여러번 구한다면 배열에 저장하여 재사용하는것이 좋다


def fibo(x):
    global arr
    # base case
    if arr[x] != -1:
        return arr[x]
    
    # recursive case
    arr[x] = fibo(x - 1) + fibo(x - 2)
    return arr[x]


n = int(input())
arr = [-1] * (n + 2)
arr[0] = 0
arr[1] = 1

print(fibo(n))
