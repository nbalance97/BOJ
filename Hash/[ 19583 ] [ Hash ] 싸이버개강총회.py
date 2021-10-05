import sys

def htom(s):
    return 60 * int(s[:2]) + int(s[3:])

start, end, finish = map(htom, input().split())
user_dict = {}
answer = 0
while True:
    try:
        time, user = input().split()
        time = htom(time)
        if time <= start:
            user_dict[user] = 1
        elif end <= time and time <= finish:
            if user_dict.get(user) != None and user_dict[user] == 1:
                user_dict[user] = 0
                answer += 1
    except:
        break
    
print(answer)
