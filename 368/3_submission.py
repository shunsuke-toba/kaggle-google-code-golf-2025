r=range(100)
def p(g):
 g=sum(g,[]);a=[i for i in r if g[i]%5]
 for i in r:
  for s in a*(g[i]==5):g[i+s-a[0]]=g[s]
 return list(zip(*[iter(g)]*10))