from collections import deque


N = int(input())
students = list(map(int, input().split()))

number = 1
stack = deque()
for student in students:
    while stack and stack[-1] == number:
        stack.pop()
        number += 1
    
    if student != number:
        stack.append(student)
    else:
        number += 1

endflag = False
while stack:
    t = stack.pop()
    if t != number:
        print("Sad")
        endflag = True
        break
    number += 1

if not endflag:
    print("Nice")
