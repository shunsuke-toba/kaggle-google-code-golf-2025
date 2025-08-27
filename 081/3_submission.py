def p(g):
 for i in range(36):l=g[y:=i//6][(x:=i%6):x+2]+g[y+1][x:x+2];g[y+(i:=l.index(0))//2][x+i%2]+=sum(l)>23
 return g