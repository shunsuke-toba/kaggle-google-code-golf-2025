def p(g):
 n=len(g);R=range(-2,3)
 for k in 2,3:
  a=[(i,j)for i in range(n) for j in range(n) if g[i][j]==k];B=s=()
  for i,j in a:
   t=[(x,y,g[i+x][j+y])for x in R for y in R if 0<=i+x<n>j+y>=0 and 0<(v:=g[i+x][j+y])!=k]
   if len(t)>len(B):c=sorted(v for*_,v in t)[len(t)//2];B=[(x,y)for x,y,v in t if v==c];s=i,j
  m=k*2-5
  for i,j in a:
   if(i,j)!=s:
    for x,y in B:g[i+x][j+y*m]=c
 return g
