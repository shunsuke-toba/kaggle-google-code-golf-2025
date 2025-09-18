def p(g,e=enumerate):
 (a,b),(d,e)=[(a,b)for a,r in e(g)for b,v in e(r)if v];h=e-b>>1
 if a-d:return[*map(list,zip(*p(list(map(list,zip(*g))))))]
 x,s=b,1
 for r in g[a-2:a+3]:g[a-2][u:=x+s*h]=g[a+2][u]=r[u-s]=g[a][x];g[a][x:u:s]=[g[a][x]]*h
 x,s=e,-1
 for r in g[a-2:a+3]:g[a-2][u:=x+s*h]=g[a+2][u]=r[u-s]=g[a][x];g[a][x:u:s]=[g[a][x]]*h
 return g