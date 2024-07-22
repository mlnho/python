H,M = map(int,input().split())

time = int(input())

M = M + time

if M >= 60:
    H += int(M / 60)
    M = int(M % 60)
    if H >= 24:
        H = H - 24

print(H,M)