#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10988                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10988                          #+#        #+#      #+#     #
#    Solved: 2024/09/02 23:37:49 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

word = input()

word_2 = ''.join(reversed(word))

if(word == word_2):
    print(1)
else :
    print(0)
