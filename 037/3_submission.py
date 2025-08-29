def p(g):
 f=sum(g,[]);d=f.index
 for v in{*f}-{0}:
  i=d(v);j=d(v,i+1)
  while j>i:j-=9+2*(j%9!=i%9);g[j//10][j%10]=v
 return g