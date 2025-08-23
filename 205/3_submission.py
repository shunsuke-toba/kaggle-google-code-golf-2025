def p(g):
 R=range;S=R(6,11);_,a,b,c,d=max((i*j,y,y+i,x,x+j)for i in S for j in S for y in R(len(g)-i+1)for x in R(len(g[0])-j+1)if sum(g[Y][X]!=g[y][x] for Y in R(y,y+i)for X in R(x,x+j))<4);g=[r[c:d]for r in g[a:b]];B=g[0][0]
 for y,x,v in[(y,x,v)for y,r in enumerate(g)for x,v in enumerate(r)if v!=B]:[r.__setitem__(x,v)for r in g];g[y]=[v]*(d-c)
 return g
