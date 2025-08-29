def p(g,e=enumerate):
 (a,b),(d,e)=[(i,j)for i,r in e(g)for j,v in e(r)if v];h=e-b>>1
 if a-d:return[*zip(*p([*map(list,zip(*g))]))]
 for x,s in(b,1),(e,-1):
  u=x+s*h;g[a][x:u:s]=[z:=g[a][x]]*h
  for r in g[a-2:a+3]:r[u-s]=g[a-2][u]=g[a+2][u]=z
 return g