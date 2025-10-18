def p(g,z=36):
 while z:z-=1;x=z%6;a,b=g[Y:=z//6][x:x+2];c,d=g[Y+1][x:x+2];g[Y+(c!=d)][x+(b!=d)]+=a&d!=c&b
 return g