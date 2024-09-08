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

score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

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
