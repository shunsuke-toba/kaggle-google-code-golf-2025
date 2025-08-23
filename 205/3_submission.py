def p(g):
 R=range;h=len(g);w=len(g[0]);_,a,b,c,d,B=max((i*j,y,y+i,x,x+j,g[y][x])for i in R(6,11)for j in R(6,11)for y in R(h-i+1)for x in R(w-j+1)if sum(g[Y][X]!=g[y][x]for Y in R(y,y+i)for X in R(x,x+j))<4);g=[r[c:d]for r in g[a:b]];w=d-c
 for y,x,v in[(y,x,v)for y,r in enumerate(g)for x,v in enumerate(r)if v!=B]:[r.__setitem__(x,v)for r in g];g[y]=[v]*w
 return g
