def p(g):
 n=len(g);r=range(n);R=range(-2,3)
 for k,m in(2,-1),(3,1):
  a=[(i,j)for i in r for j in r if g[i][j]==k];B=s=C=()
  for i,j in a:
   t=[(x,y,g[i+x][j+y])for x in R for y in R if n>i+x>=0<=j+y<n and 0<(v:=g[i+x][j+y])!=k]
   if t:
    V=[v for*_,v in t];c=max(V,key=V.count);d=[(x,y)for x,y,v in t if v==c]
    if len(d)>len(B):B=d;s=(i,j);C=c
  if B:
   a.remove(s)
   for i,j in a:
    for x,y in B:g[i+x][j+y*m]=C
 return g
