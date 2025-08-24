E=enumerate
def p(g):
 for y,r in E(g):
  for x,v in E(r):
   if 0<v<3:
    for i in-1,1:g[y+i][x+w*i]=g[y+w*i][x+i-2*w*i]=7-3*(w:=v>1)
 return g
