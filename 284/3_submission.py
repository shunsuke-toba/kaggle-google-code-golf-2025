def p(g):
 (a,b,c),(d,e,f)=[(i,j,v)for i,r in enumerate(g)for j,v in enumerate(r)if v]
 if a-d:return[*zip(*p([*map(list,zip(*g))]))]
 h=e-b-1>>1
 for x,z,s in(b,c,1),(e,f,-1):
  u=x+s*(h-1)
  g[a][x:x+s*h:s]=[z]*h
  for r in g[a-2:a+3]:r[u]=g[a-2][u+s]=g[a+2][u+s]=z
 return g
