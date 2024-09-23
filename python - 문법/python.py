# 2차원 배열 선언법

array = [[0]*4 for _ in range(100)] # 100행 4열 2차원 배열이 선언된다.

print(array)


# 리스트 비어있는지 체크
if not list:
    print("this is empty")
    
    
# ASCII 코드
# 대문자 - 65 , 소문자 - 97
# 문자를 숫자로
print("ord :",ord('a')) # 97
# 숫자륾 문자로
print("chr :",chr(97)) # a



# 내림차순
list.sort(reverse=True)

# 입력받은 숫자 리스트로 전환
A = int(input)
print("입력받은 숫자 -> 리스트 : ", list(str(A)))