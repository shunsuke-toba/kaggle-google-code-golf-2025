def p(g,e=enumerate):
 (a,b),(d,e)=[(i,j)for i,r in e(g)for j,v in e(r)if v];h=e-b>>1
 if a-d:return[*zip(*p([*map(list,zip(*g))]))]
 for x,s in(b,1),(e,-1):
  for r in g[a-2:a+3]:r[(u:=x+s*h)-s]=g[a-2][u]=g[a+2][u]=z=g[a][x];g[a][x:u:s]=[z]*h
 return g