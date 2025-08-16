from collections import*
def p(g):
 c=min((v,k)for k,v in Counter(sum(g,[])).items()if k)
 g=[r for r in g if c[1]in r]
 e=[i for r in g for i,x in enumerate(r)if x==c[1]]
 return[r[min(e):max(e)+1]for r in g]
