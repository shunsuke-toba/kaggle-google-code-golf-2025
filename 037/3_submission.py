def p(g):
 for j,v in enumerate(f:=sum(g,[])):
  while v and j>(i:=f.index(v)):j-=9+2*(j%9!=i%9);g[j//10][j%10]=v
 return g