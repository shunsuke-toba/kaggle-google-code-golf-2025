def p(g):
 b={};h=len(g);w=len(g[0])
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v:
    t=b.setdefault(v,[y,x,y,x]);y<t[0]and t.__setitem__(0,y);x<t[1]and t.__setitem__(1,x);y>t[2]and t.__setitem__(2,y);x>t[3]and t.__setitem__(3,x)
 P=B=None
 for c,(a,l,d,r) in b.items():
  if all(g[i][j]==c for i in range(a,d+1)for j in range(l,r+1)):B=(c,a,l,d,r)
  else:P=c
 s=b[P][1]+b[P][3]
 if B:
  c,a,l,d,r=B
  for y in range(h):
   if y<a or y>d:
    L=[j for j,v in enumerate(g[y])if v==P]
    if L:s=min(L)+max(L);break
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v and v!=P:
    j=s-x;r[x]=0<=j<w and g[y][j]
 return g
