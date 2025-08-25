def p(g):
 (a,b,c),(d,e,f)=[(i,j,v)for i,r in enumerate(g)for j,v in enumerate(r)if v]
 if a-d:return[*zip(*p([*map(list,zip(*g))]))]
 for x,y,z,s in(b,e,c,1),(e,b,f,-1):
  u=x+y-3*s>>1
  g[a][x:u+s:s]=[z]*-~((u-x)*s)
  for r in g[a-2:a+3]:r[u]=g[a-2][u+s]=g[a+2][u+s]=z
 return g