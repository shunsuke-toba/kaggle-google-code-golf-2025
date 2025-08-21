def p(g):
 h,w=len(g),len(g[0])
 for k,m in(2,-1),(3,1):
  a=[(i,j)for i in range(h)for j in range(w)if g[i][j]==k];B=s=C=()
  for i,j in a:
   t=[(x,y,g[i+x][j+y])for x in range(-2,3)for y in range(-2,3)if 0<=i+x<h and 0<=j+y<w and(v:=g[i+x][j+y])and v!=k]
   if t:
    V=[v for _,_,v in t];c=max(V,key=V.count);d=[(x,y)for x,y,v in t if v==c]
    if len(d)>len(B):B=d;s=(i,j);C=c
  if B:
   a.remove(s)
   for i,j in a:
    for x,y in B:g[i+x][j+y*m]=C
 return g
