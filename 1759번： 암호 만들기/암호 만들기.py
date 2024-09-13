#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1759                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1759                           #+#        #+#      #+#     #
#    Solved: 2024/09/13 23:23:17 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 자음 : con
# 모음 : gather


def needWord():
    global answer, L

    # 모음 1개이상
    # 자음 2개이상
    gather = 0  # 모음
    con = 0  # 자음

    alpha = ["a", "e", "i", "o", "u"]

    for i in answer:
        gather += i in alpha # 모음
    
    con = L - gather # 자음

    return gather >= 1 and con >= 2


def combination(index, level):
    global L, C, word, answer

    # base case
    if level == L:
        if needWord():
            print("".join(answer))  # 리스트 붙여서 출력하는 법
        return
    # recursive case
    for i in range(index, C):
        answer.append(word[i])
        combination(i + 1, level + 1)
        answer.pop()


# C개의 문자들이 공백으로 구분되어 주어짐
L, C = map(int, input().split())

# 알파벳 정렬
# sorted : 새로운 정렬된 리스트를 생성
word = input().split()
word.sort()


# 최종
answer = []
combination(0, 0)
