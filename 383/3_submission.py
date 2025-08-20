def p(g):
 h=len(g);w=len(g[0]);a=h;b=0;c=w;d=0
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v:a=min(a,y);b=max(b,y);c=min(c,x);d=max(d,x)
 t=g[a][c];r=[r[:]for r in g]
 for y in range(a,b+1):
  for x in range(c,d+1):
   v=g[y][x]
   if v!=t:
    if y-a<2 or b-y<2:
     for i in range(h):r[i][x]=[v,t][a<=i<=b]
    if x-c<2 or d-x<2:
     for j in range(w):r[y][j]=[v,t][c<=j<=d]
 return r
