def p(g):
 (a,b,c),(d,e,f)=[(i,j,v)for i,r in enumerate(g)for j,v in enumerate(r)if v]
 if(t:=b==e):_=lambda:[*map(list,zip(*g))];g=_();a,b,e=b,a,d
 for x,y,z in(b,e,c),(e,b,f):
  s=1-2*(y<x);u=x+y-3*s>>1
  g[a][x:u+s:s]=[z]*-~((u-x)*s)
  for r in g[a-2:a+3]:r[u]=g[a-2][u+s]=g[a+2][u+s]=z
 return t and _()or g
