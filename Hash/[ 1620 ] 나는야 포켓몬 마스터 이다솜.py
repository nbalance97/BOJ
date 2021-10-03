import sys

input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())

num_to_pokemon = {}
pokemon_to_num = {}
idx = 1

for _ in range(n):
    pokemon = input()
    num_to_pokemon[idx] = pokemon
    pokemon_to_num[pokemon] = idx
    idx += 1

for _ in range(m):
    question = input()
    if question.isdigit():
        print(num_to_pokemon[int(question)])
    else:
        print(pokemon_to_num[question])


        
