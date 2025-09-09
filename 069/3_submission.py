def p(g):
 g=sum(g,[]);r=range(100);p=[i for i in r if g[i]%8]
 for i in r:
  for j in p*(g[i]==8):g[i+j-p[0]]=g[j]
 for j in p:g[j]=0
 return*zip(*[iter(g)]*10),