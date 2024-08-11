import sys

read = sys.stdin.readline

student = []
for i in range(1, 31):
    student.append(i)

for i in range(28):
    number = int(read())
    student.remove(number)

print(min(student))
print(max(student))
