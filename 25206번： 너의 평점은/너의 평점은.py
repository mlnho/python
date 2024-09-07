#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25206                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25206                          #+#        #+#      #+#     #
#    Solved: 2024/09/07 19:11:42 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

score = {}

score["A+"] = 4.5
score["A0"] = 4.0
score["B+"] = 3.5
score["B0"] = 3.0
score["C+"] = 2.5
score["C0"] = 2.0
score["D+"] = 1.5
score["D0"] = 1.0
score["F"] = 0.0

# 3.0 ..... -- 학점의 총합
userScore = 0
# A+ .....
gradeScore = 0


## 전공평점 : 과목별의 합을 학점의 총합으로 나눈 값
for i in range(20):
    user = input().split()
    # 학점의 총합 : userScor
    # P 제외 점수계산
    if user[2] in score:
        userScore += float(user[1])
        gradeScore += float(user[1]) * score[user[2]]

answer = gradeScore / userScore

# 6자리 수 출력을 위한 format(number,'.6f)
print(format(answer, ".6f"))
