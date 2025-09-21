def p(g):
 g=sum(g,[]);r=range(100);p=[i for i in r if g[i]%8];h=[0]*100
 for i in r:
  for j in(g[i]==8-h[i])*p:h[i+j-p[0]]=g[j]
 return*zip(*[iter(h)]*10),