#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 6603                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/6603                           #+#        #+#      #+#     #
#    Solved: 2024/09/13 22:58:21 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


def combination(index,level):
    global user,k,choose
    
    # 뽑는 개수는 6개로 고정
    # base case
    if level == 6:
        print(*choose)
        return
    
    for i in range(index,k):
        choose.append(arr[i])
        combination(i+1,level+1)
        choose.pop()



# 입력받는 코드
# 0을 만나면 Stop
while True:
    choose = []
    user = list(map(int,input().split()))
    # 첫번째 수 : k
    k = user[0]
    # 리스트는 1번째 인덱스부터 쭉
    arr = user[1:]
    
    if k == 0:
        break
    
    combination(0,0)
    print()

