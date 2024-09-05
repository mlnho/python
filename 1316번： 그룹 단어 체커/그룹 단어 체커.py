#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1316                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1316                           #+#        #+#      #+#     #
#    Solved: 2024/09/05 15:25:10 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


N = int(input())

answer = 0
for i in range(N):
    word = list(input())
    # print(word)
    for j in range(len(word) - 1):
        if word[j] == word[j + 1]:
            continue
        elif word[j] in word[j + 1 :]:
            break
    else:
        answer += 1

print(answer)
