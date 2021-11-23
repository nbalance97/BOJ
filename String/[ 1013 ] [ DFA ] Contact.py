import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
total_case = list()
for _ in range(n):
    s = input()
    automata = 'S'
    for ch in s:
        if automata == 'S':
            if ch == '1':
                automata = 1
            else:
                automata = 2
                
        elif automata == 1:
            if ch == '1':
                print('NO')
                break
            else:
                automata = 3
                
        elif automata == 2:
            if ch == '1':
                automata = 7
            else:
                print('NO')
                break
            
        elif automata == 3:
            if ch == '0':
                automata = 4
            else:
                print('NO')
                break
            
        elif automata == 4:
            if ch == '0':
                continue
            else:
                automata = 5
                
        elif automata == 5:
            if ch == '0':
                automata = 2
            else:
                automata = 6
                
        elif automata == 6:
            if ch == '0':
                automata = 8
            else:
                continue
            
        elif automata == 7:
            if ch == '0':
                automata = 2
            else:
                automata = 1
                
        elif automata == 8:
            if ch == '0':
                automata = 4
            else:
                automata = 7
    else:
        if automata == 7 or automata == 5 or automata == 6:
            print('YES')
        else:
            print('NO')

                
            
