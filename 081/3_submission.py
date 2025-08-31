def p(g):
 for y in range(36):x=y%6;y//=6;l=g[y][x:x+2]+g[y+1][x:x+2];i=l.index(0);g[y+i//2][x+i%2]=sum(l)>16
 return g