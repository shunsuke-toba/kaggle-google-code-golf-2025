def p(g):
 h=len(g);w=len(g[0]);W=w+2
 G=[0]*W+sum(([0,*r,0]for r in g),[])+[0]*W
 P=range(W+1,W*(h+1)-1)
 D=(1,W,W+1,W-1)
 T=[(d,a,b)for j in P if(b:=G[j])for d in D if(a:=G[j+d])*(a-b)and G[j-d]==a]
 for j in P:
  for d,a,c in T:
   if G[j]==c:G[j+d]=G[j-d]=a
   elif G[j+d]==G[j-d]==a:G[j]=c
 return[G[i:i+w]for i in range(W+1,W*(h+1)-1,W)]
