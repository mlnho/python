N = int(input())

byte = N//4

answer = str("")

for i in range(byte):
    answer += 'long '

print(answer+'int')
