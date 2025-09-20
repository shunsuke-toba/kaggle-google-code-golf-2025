def p(g):
 for _ in[0]*4:c,d=map([*map(max,g:=[*zip(*g[::-1])])].index,(8,2));g+=g[c+2:d];g[c+2:d]=[]
 return g