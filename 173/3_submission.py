def p(g):
 w=len(g[0]);W=w+2;G=[0]*W+sum(([0,*r,0]for r in g),[])+[0]*W;P=[W+1+i+i//w*2 for i in range(w*len(g))]
 T=[(d,a,b)for j in P if(b:=G[j])for d in((1,-1,W,-W),(W+1,W-1,-W+1,-W-1),(1,-1),(W,-W))if(a:=G[j+d[0]])and a-b and all(G[j+x]==a for x in d[1:])]
 for j in P:
  for d,a,b in T:
   if G[j]==b:
    for x in d:G[j+x]=G[j+x]or a
   elif all(G[j+x]==a for x in d):G[j]=b
 return[G[j:j+w]for j in P[::w]]
