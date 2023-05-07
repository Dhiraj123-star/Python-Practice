from itertools import combinations

programming_langs = ['Python','Java','C++']

comb = combinations(programming_langs,2)

for c in comb:
    print(c)