H,M = map(int,input().split())

if M<45:
    H = H - 1
    M = M + 60 - 45
    if H < 0:
        H = H + 24
else:
    M = M - 45

print(H,M)