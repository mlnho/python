#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1475                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1475                           #+#        #+#      #+#     #
#    Solved: 2024/09/23 21:27:27 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


def test(roomNumber):
    numbers = [0] * 10

    # 6과 9 균형을 맞춘다,,, 많은 수를 채택하는 방법
    for i in roomNumber:
        if i == "6" or i == "9":
            if numbers[6] <= numbers[9]:
                numbers[6] += 1
                print(numbers)
            elif numbers[6] >= numbers[9]:
                numbers[9] += 1
                print(numbers)
        else:
            numbers[int(i)] += 1

    # print(numbers)
    print(max(numbers))


test(input())
