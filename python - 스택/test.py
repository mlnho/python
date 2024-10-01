from collections import deque

# # 스택 선언
st = deque()

# 맨 위(뒤)에 원소 추가
st.append(10)
st.append(20)
st.append(30)

# 스택 출력
print("스택:", st)
print()

# 맨 위(뒤)의 원소 제거
removed_element = st.pop()
print("삭제된 원소:", removed_element)
print("삭제 후 스택:", st)
print()

# 맨 위(뒤)의 원소 확인
top_element = st[-1]
print("맨 위(뒤)의 원소:", top_element)
print("현재 스택:", st)
print()

# 스택의 크기 확인
print("스택의 크기:", len(st))
print()

# 스택이 비어 있는지 확인
print("스택이 비어 있는지 확인:", not st) # 비어있지 않으면 True 
print()

# # 스택 순회
while st:
    print(st.pop(), end=' ')
    
    
    
    
    
# BOJ 10828 : 기본 스택

import sys  # 시간초과가 났어서 sys로 수정

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    lst = list(sys.stdin.readline().split())  # 입력 값 받기
    if "push" in lst:
        stack.append(lst[1])
        # print('현재 stack :',stack)
    elif "pop" in lst:
        if len(stack) == 0:  # stack 이 빈 리스트일 경우에
            print(-1)
        else:
            print(stack.pop())
    elif "size" in lst:
        print(len(stack))
    elif "empty" in lst:
        if len(stack) == 0:  # stack 이 빈 리스트일 경우에
            print(1)
        else:
            print(0)
    elif "top" in lst:
        if len(stack) == 0:  # stack 이 빈 리스트일 경우에
            print(-1)
        else:
            print(stack[-1])
