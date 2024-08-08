
import itertools
n=input()
res=list(itertools.permutations(n))
for i in res:
    print(''.join(i))
