def p(g):
 (a,b),(d,e)=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v]
 if a-d:return[*zip(*p([*map(list,zip(*g))]))]
 h=e-b>>1
 for x,s in(b,1),(e,-1):
  z=g[a][x];u=x+s*h;g[a][x:u:s]=[z]*h
  for r in g[a-2:a+3]:r[u-s]=g[a-2][u]=g[a+2][u]=z
 return g