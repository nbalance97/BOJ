import sys
N = 0

for i in range(100):
    try:
        string = input()
        lower, upper, digit, blank = 0, 0, 0, 0
        for char in string:
            if char == " ":
                blank += 1
            if char.isupper():
                upper += 1
            if char.islower():
                lower += 1
            if char.isdigit():
                digit += 1

        print("%d %d %d %d"%(lower, upper, digit, blank))
    except EOFError:
        break
