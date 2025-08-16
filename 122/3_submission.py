def p(g):
 for y,r in enumerate(g):
  if 2 in r:x=r.index(2);break
 d=x+3<len(g[0])and g[y+1][x+3]==3
 for r in g[y:y+3]:r[x:x+3]=[0]*3
 X=x+2*d;Y=y+2-2*d
 for r in g[Y:Y+3]:r[X:X+3]=[2]*3
 g[y+1][x+1]=g[Y+1][X+1]=3
 return g
