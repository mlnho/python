#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1157                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1157                           #+#        #+#      #+#     #
#    Solved: 2024/09/03 22:35:03 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 알파벳 리스트 26개
alphabet = ["a","b","c","d","e","f","g","h",
            "i","j","k","l","m","n","o","p","q",
            "r","s","t","u","v","w","x","y","z",]

lst = [0]*26

# print("lst 길이:",len(lst))

word = input()

word = word.lower() # 소문자 전환

for i in range(len(word)):
    for j in range(26):
        if word[i] == alphabet[j]:
            lst[j] += 1


# print(lst)

answer = "?"

max = 0
for i in range(len(lst)):
    if lst[i] > max:
        max = lst[i]
        answer = alphabet[i]
    elif max == lst[i]:
        answer = "?"
        


print(answer.upper())
