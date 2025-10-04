def p(g):
 for y in range(36):x=y%6;y//=6;a,b=g[y][x:x+2];c,d=g[y+1][x:x+2];g[y+(c!=d)][x+(b!=d)]+=a&d!=c&b
 return g