
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