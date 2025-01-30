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


word = input().upper()  # 결과물 대문자이기에 대문자로 지정

word_lst = list(set(word))  # set은 순서를 보장하지 않고 중복을 제거 -> list로 변환
print("word_lst:",word_lst)

cnt = []  # 문자를 저장할 리스트

for i in word_lst:
    count = word.count(i)  # word 문자에 word_lst(i)가 몇개 들어가는지 체크
    print("count:", count)
    cnt.append(count)  # 센 결과값을 cnt에 추가
    
print("cnt:",cnt)

if (cnt.count(max(cnt))) > 1: #cnt에서 최댓값 개수가 1개 초과되면 "?" 출력
    print("?")
else:
    print(word_lst[(cnt.index(max(cnt)))])
