def p(g):
 for i in range(81):
  for X in(-1,1)[(w:=g[y:=i//9][x:=i%9]-1)&6:]:g[y+X][x+w*X]=g[y-w*X][x+X]=7-3*w
 return g