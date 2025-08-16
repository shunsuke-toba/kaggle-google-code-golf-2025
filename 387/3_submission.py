def p(g):
 p=[(i,j,v)for i,r in enumerate(g)for j,v in enumerate(r)if v];a,b={v for *_,v in p};y,x,_=zip(*p);Y=max(y);y=min(y);X=max(x);x=min(x);r=[[0]*len(g[0])for _ in g]
 for j in range(x+1,X):r[y][j]=r[Y][j]=5*(~min(j-x,X-j)&1)
 for i in range(y+1,Y):r[i][x]=r[i][X]=5*(~min(i-y,Y-i)&1)
 for i,j,v in p:
  o=a^b^v
  for I in i-1,i,i+1:r[I][j-1:j+2]=[o]*3
  r[i][j]=v
 return r
