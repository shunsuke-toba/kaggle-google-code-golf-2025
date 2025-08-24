def p(g):
 (y,x,a),(y,X,b),(Y,x,_),_=p=[(i,j,v)for i,r in enumerate(g)for j,v in enumerate(r)if v]
 for i in range(x+1,X):g[y][i]=g[Y][i]=5*(~min(i-x,X-i)&1)
 for i in range(y+1,Y):g[i][x]=g[i][X]=5*(~min(i-y,Y-i)&1)
 for i,j,v in p:
  for r in g[i-1:i+2]:r[j-1:j+2]=[a^b^v]*3;g[i][j]=v
 return g

