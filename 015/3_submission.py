def p(g):
 for i in range(81):
  if -1<(w:=g[y:=i//9][x:=i%9]-1)<2:g[y+1][x+w]=g[y-1][x-w]=g[y+w][x-1]=g[y-w][x+1]=7-3*w
 return g