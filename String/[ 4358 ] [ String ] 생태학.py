
from collections import defaultdict

count = defaultdict(lambda: 0)
total_count = 0
while True:
    try:
        name = input()
        total_count += 1
        count[name] += 1
    except:
        break

for p in sorted(count.keys()):
    k = round(count[p] / total_count * 100, 4)
    print("%s %.4f"%(p, k))
    

