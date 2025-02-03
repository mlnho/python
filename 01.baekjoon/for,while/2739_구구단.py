# N 입력받기 -> 구구단 N단 출력



def multiple():
    N = int(input())
    for i in range(1,10):
        # print(N,"*",i ,"=",N*i)
        print(f"{N} * {i} = {N*i}")


N = multiple()
