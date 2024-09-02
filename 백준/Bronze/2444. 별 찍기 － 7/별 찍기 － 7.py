N = int(input()) # 5

for i in range(1,N+1):
    print(" "* (N-i) + "*" * (i*2-1))

for i in range(N-1,0,-1):
    print( (" " * (N-i) ) + "*" * (i*2-1) )