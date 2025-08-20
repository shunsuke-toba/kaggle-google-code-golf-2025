def p(g):
 h=len(g);w=len(g[0]);r=range;x,y=zip(*((i,j)for i in r(h)for j in r(w)if g[i][j]<1));a=min(x);b=max(x);c=min(y);d=max(y);R=C=1
 while any(g[i][j]-g[i%R][j]for i in r(h)for j in r(w)if j<c or j>d):R+=1
 while any(g[i][j]-g[i][j%C]for i in r(h)for j in r(w)if i<a or i>b):C+=1
 t=[[0]*C for _ in r(R)]
 for i in r(h):
  for j in r(w):
   if i<a or i>b or j<c or j>d:t[i%R][j%C]=g[i][j]
 return[[t[i%R][j%C]for j in r(c,d+1)]for i in r(a,b+1)]
