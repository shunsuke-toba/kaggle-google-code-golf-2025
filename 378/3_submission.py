def p(g):
 m=~-len(g);i=m*m
 while i:=i-1:
  t=g[y:=i//m];d=g[y+1][z:=i%m]>0 or-1;e=t[z+1]>0;e-=t[z-1]>0;y*=e&(t[z]>g[a:=y+d][b:=z+e])
  while 0<y<m>z>0:g[y:=y-d][z:=z-e]=g[a+d][b+e]
 return g