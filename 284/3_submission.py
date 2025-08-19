def p(g):
 (a,b,c),(d,e,f)=[(i,j,v)for i,r in enumerate(g)for j,v in enumerate(r)if v]
 if(t:=b==e):_=lambda:[*map(list,zip(*g))];g=_();a,b,d,e=b,a,e,d
 for x,y,z in(b,e,c),(e,b,f):
  s=1-2*(y<x);l=(y-x)*s-3>>1;u=x+s*l
  g[a][x:u+s:s]=[z]*-~l
  for r in g[a-2:a+3]:r[u]=z
  g[a-2][u+s]=g[a+2][u+s]=z
 return t and _()or g
