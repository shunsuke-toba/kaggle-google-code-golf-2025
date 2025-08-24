def p(g):
 f=sum(g,[]);d=f.index
 for v in {*f}-{0}:
  i=d(v);j=d(v,i+1);s=9+2*(j%10>i%10)
  while j>=i:g[j//10][j%10]=v;j-=s
 return g

