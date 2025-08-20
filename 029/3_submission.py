def p(g,R=range,E=enumerate):
 d={}
 for i,r in E(g):
  for j,v in E(r):
   x,y,X,Y=d.get(v,(i,j,i,j));d[v]=min(x,i),min(y,j),max(X,i),max(Y,j)
 for v,(a,c,b,d) in d.items():
  if b-a>1 and d-c>1 and all(g[a][k]==v==g[b][k]for k in R(c,d+1))and all(g[k][c]==v==g[k][d]for k in R(a,b+1)):
   return[r[c+1:d]for r in g[a+1:b]]
