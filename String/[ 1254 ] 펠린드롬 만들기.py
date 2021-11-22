
def check(a):
    return a == a[::-1]

s = input()
if len(s) == 1:
    print(1)
else:
    for i in range(1, len(s)+1):
        new = s[:i] + (s[:i])[::-1]
        if len(new) >= len(s) and new[:len(s)] == s and check(new):
            print(len(new))
            break

        new = s[:i] + s[i] + (s[:i])[::-1]
        if len(new) >= len(s) and new[:len(s)] == s and check(new):
            print(len(new))
            break
    
    
        
