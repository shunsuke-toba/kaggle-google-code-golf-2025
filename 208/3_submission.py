def p(g):
 s=[v for r in g for v in r if v]
 k=min(s,key=s.count)
 I=range;h=len(g);w=len(g[0])
 i=[r for r in I(h)if k in g[r]]
 u,v=i[0],i[-1]
 j=[c for c in I(w)if any(g[r][c]==k for r in i)]
 l,r=j[0],j[-1];H=v-u+1;W=r-l+1
 for y in I(h-H+1):
  for x in I(w-W+1):
   if(x-l|y-u)and all(g[Y][X]<1 for Y in I(y+1,y+H-1)for X in I(x+1,x+W-1)):
    for t in I(H):g[y+t][x:x+W]=g[u+t][l:l+W]
    return g
