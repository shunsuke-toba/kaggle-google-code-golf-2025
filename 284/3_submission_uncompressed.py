def p(g,e=enumerate):
 (i,a),(f,d)=[(i,a)for i,r in e(g)for a,v in e(r)if v];h=d-a>>1
 if i-f:return[*map(list,zip(*p(list(map(list,zip(*g))))))]
 x,s=a,1
 for r in g[i-2:i+3]:g[i-2][u:=x+s*h]=g[i+2][u]=r[u-s]=g[i][x];g[i][x:u:s]=[g[i][x]]*h
 x,s=d,-1
 for r in g[i-2:i+3]:g[i-2][u:=x+s*h]=g[i+2][u]=r[u-s]=g[i][x];g[i][x:u:s]=[g[i][x]]*h
 return g