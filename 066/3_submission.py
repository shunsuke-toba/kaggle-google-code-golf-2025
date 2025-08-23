def p(g):
 (a,b),(c,d)=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==3]
 f=lambda y,x,A,B,t=2:(y:=y+A,x:=x+B,len(g)>y>=0<=x<len(g[0])and((v:=g[y][x])==2 or v==8 and t and(f(y-A,x-B,B,-A,t-1)or f(y-A,x-B,-B,A,t-1)) or v-8 and f(y,x,A,B,t)and(g[y].__setitem__(x,3)or 1)))[2]
 for y,x,A,B in(((a,b,0,-1),(c,d,0,1)),((a,b,-1,0),(c,d,1,0)))[a!=c]:
  if g[y+A][x+B]-8 and f(y,x,A,B):break
 return g