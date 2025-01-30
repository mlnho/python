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
    numbers = [0] * 9  # 9는 6과 동일 예정
    room_list = list(str(roomNumber))

    # print(room_list)

    # 0~8의미하며 9는 6과 동일 취급할 예정
    for number in room_list:
        if int(number) == 9:
            numbers[6] += 1
        else:
            numbers[int(number)] += 1

    if numbers[6] >= 2 and numbers[6] % 2 == 0:
        numbers[6] = numbers[6] // 2
    elif numbers[6] >= 2 and numbers[6] % 2 != 0:
        numbers[6] = numbers[6] // 2 + 1

    # print("numbers :", numbers)
    print(max(numbers))


test(int(input()))
