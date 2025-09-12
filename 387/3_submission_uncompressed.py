def p(g):
 e=enumerate;(y,x,a),(y,X,b),(Y,x,_),_=p=[(i,j,v)for i,r in e(g)for j,v in e(r)if v]
 for i in range(x,X+1):g[y][i]=g[Y][i]=~min(i-x,X-i)%2*5
 for i in range(y,Y+1):g[i][x]=g[i][X]=~min(i-y,Y-i)%2*5
 for i,j,v in p:
  for r in g[i-1:i+2]:r[j-1:j+2]=[a^b^v]*3;g[i][j]=v
 return g