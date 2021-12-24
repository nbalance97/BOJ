import sys

input = lambda: sys.stdin.readline().rstrip()
color = ['black', 'brown', 'red', 'orange', 'yellow', 'green',
         'blue', 'violet', 'grey', 'white']
value_dict = {c:i for i, c in enumerate(color)}
multiply_dict = {c:10**i for i, c in enumerate(color)}

answer = 0
color1 = input()
color2 = input()
color3 = input()

answer = value_dict[color1] * 10 + value_dict[color2]
answer *= multiply_dict[color3]

print(answer)

