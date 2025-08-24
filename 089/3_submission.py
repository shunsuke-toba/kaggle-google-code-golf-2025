R=range(-2,3)
def p(g):
 for k in 2,3:
  a=[divmod(t,13)for t in range(169)if g[t//13][t%13]==k];B=s=()
  for i,j in a:
   t=[(v,x,y)for x in R for y in R if 13>i+x>-1<j+y<13 and 0<(v:=g[i+x][j+y])!=k]
   if len(t)>len(B):c=sorted(t)[len(t)//2][0];B=[(x,y)for v,x,y in t if v==c];s=i,j
  if a:a.remove(s)
  for i,j in a:
   for x,y in B:g[i+x][j+y*(k*2-5)]=c
 return g
