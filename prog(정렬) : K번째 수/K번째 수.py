# array	commands	return
# [1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]


def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        test = []
        a = commands[i][0] - 1
        b = commands[i][1] - 1
        c = commands[i][2] - 1
        # print(a,b,c)
        for j in range(a, b + 1):
            test.append(array[j])
            # print("test : ", test)
        test.sort()
        answer.append(test[c])
        # print("answer : ", answer)

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


# 풀이 후기
# 1. print 찍어보면서 확인해보자
# 이런 문제 배열의 끝에 +1 하는걸 잊지말자,,