def p(g):
 g=sum(g,[]);r=range(100);p=[i for i in r if g[i]%8];b=p[0]
 for i in r:
  if g[i]==8:
   for j in p:g[i+j-b]=g[j]
 for j in p:g[j]=0
 return*zip(*[iter(g)]*10),