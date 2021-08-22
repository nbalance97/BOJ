import sys

input = sys.stdin.readline

N = int(input().rstrip())

option_set = set()

for _ in range(N):
    options = input().rstrip('\n').split()

    end = False
    
    for i in range(len(options)):
        if options[i][0].upper() not in option_set:
            option_set.add(options[i][0].upper())
            options[i] = '[' + options[i][0] + ']' + options[i][1:]
            end = True
            break

    if not end:
        for i in range(len(options)):
            for j in range(len(options[i])):
                if options[i][j].upper() not in option_set:
                    option_set.add(options[i][j].upper())
                    options[i] = options[i][:j] + '[' + options[i][j] + ']' + options[i][j+1:]
                    end = True
                    break
            if end:
                break
            
    print(*options)
