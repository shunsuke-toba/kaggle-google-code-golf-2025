def p(g):
 W=len(g[0])+2;G=[0]*W+sum(([0,*r,0]for r in g),[])+[0]*W;P=range(W+1,~W+len(G))
 for j in P:
  for d in 1,W,W+1,W-1:
   if(a:=G[j+d])==G[j-d]!=(c:=G[j])>0<a:
    for k in P:
     if G[k]==c:G[k+d]=G[k-d]=a
     if G[k+d]==G[k-d]==a:G[k]=c
 return[G[i:i+W-2]for i in P[::W]]
