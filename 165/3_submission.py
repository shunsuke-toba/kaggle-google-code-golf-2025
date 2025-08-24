def p(g):
 k=[w for p,r in zip(g,g[1:])for v,w,x,y in zip(r,r[1:],r[2:],p[1:-1])if v==w==x==y>0][0]
 for x in range(20):
  y=20;c=0
  while y and (b:=g[y-1][x])-k:y-=1;c|=b
  for t in g[y:]*c*y:t[x]=c
 return g

