def p(g):
 W=len(g[0])+2
 G=[0]*W+sum(([0,*r,0]for r in g),[])+[0]*W
 P=range(W+1,~W+len(G))
 T=[(d,a,c)for j in P if(c:=G[j])for d in(1,W,W+1,W-1)if(a:=G[j+d])*(a-c)and G[j-d]==a]
 for j in P:
  for d,a,c in T:
   if G[j]==c:G[j+d]=G[j-d]=a
   elif G[j+d]==G[j-d]==a:G[j]=c
 return[G[i:i+W-2]for i in P[::W]]
