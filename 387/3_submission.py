def p(g):
 e=enumerate;(y,x,a),(y,X,b),(Y,x,_),_=p=[(i,j,v)for i,s in e(g)for j,v in e(s)if v];i=x
 while i<=X:g[y][i]=g[Y][i]=~min(i-x,X-i)%2*5;i+=1
 i=y
 while i<=Y:g[i][x]=g[i][X]=~min(i-y,Y-i)%2*5;i+=1
 for i,j,v in p:
  for s in g[i-1:i+2]:s[j-1:j+2]=[a^b^v]*3;g[i][j]=v
 return g
