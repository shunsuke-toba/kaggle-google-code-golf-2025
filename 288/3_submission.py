def p(g):
 k=len(g)-2;r=g[k];w=len(r);c=g[-1][w//2]
 for x in range(w):
  for d in-1,1:
   i=x+d
   if r[x]and-1<i<w and r[i]<1:
    j=k-1
    while j+1 and-1<i<w:g[j][i]=c;j-=1;i+=d
 return g
