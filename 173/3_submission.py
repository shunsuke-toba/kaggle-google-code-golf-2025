def p(g):
 W=(w:=len(g[0]))+2;G=[0]*W+sum(([0,*r,0]for r in g),[])+[0]*W;P=[W+1+i+i//w*2 for i in range(w*len(g))];T=[(d,a,b)for j in P if (b:=G[j]) for d in((1,-1,W,-W),(W+1,W-1,-W+1,-W-1),(1,-1),(W,-W)) if (a:=G[j+d[0]]) and a-b and all(G[j+x]==a for x in d[1:])]
 z=1
 while z:
  z=0
  for j in P:
   for d,a,b in T:
    if G[j]==b:
     for x in d:
      if G[j+x]<1:G[j+x]=a;z=1
    elif G[j]<1 and all(G[j+x]==a for x in d):G[j]=b;z=1
 return[G[j:j+w]for j in P[::w]]
