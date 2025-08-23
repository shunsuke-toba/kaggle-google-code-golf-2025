def p(g):
 if 5 in g[0]:return [*map(list,zip(*p([*map(list,zip(*g))])))]
 for z in range(9**5):x,y=z//14%12+1,z%14;i=x+1-2*(x<7);u=g[x][y];g[x][y]=u and 5 or g[i][y];g[i][y]*=u>0
 return g
