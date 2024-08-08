import sys

read = sys.stdin.readline


# 바구니 개수 - N
# 공 넣는 방법 - M 번

N, M = map(int,read().split())

answer = [0] * N # 배열 크기 정하기 

for o in range(M):
    i,j,k = map(int,read().split())
    for l in range(i,j+1):
        answer[l-1] = k

print(*answer) # 파이썬 리스트 출력 공백 구분 