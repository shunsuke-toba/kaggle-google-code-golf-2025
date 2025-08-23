def p(g):
 r=range;e=enumerate;S=r(6,11);_,a,b,c,d=max((i*j,y,y+i,x,x+j)for i in S for j in S for y in r(len(g)-i+1)for x in r(len(g[0])-j+1)if len({g[Y][X]for Y in r(y,y+i)for X in r(x,x+j)})<3);g=[R[c:d]for R in g[a:b]];b=g[0][0]
 for y,x,v in[(y,x,v)for y,R in e(g)for x,v in e(R)if v-b]:
  for L in g:L[x]=v
  g[y]=[v]*(d-c)
 return g