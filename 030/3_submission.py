def p(g):
 h,w=len(g),len(g[0]);b=min([r for r in range(h)for c in range(w)if g[r][c]==1]or[h]);o=[[0]*w for _ in range(h)]
 for v in[1,2,4]:
  t=[(r,c)for r in range(h)for c in range(w)if g[r][c]==v]
  if t:s=b-min(r for r,c in t);[(r+s<h)and(o[r+s].__setitem__(c,v))for r,c in t]
 return o