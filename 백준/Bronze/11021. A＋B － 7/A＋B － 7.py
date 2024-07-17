x = int(input())

word = 'Case #'
for i in range(x):
    a,b = map(int,input().split())
    print(f'Case #{i+1}: {a+b}')
