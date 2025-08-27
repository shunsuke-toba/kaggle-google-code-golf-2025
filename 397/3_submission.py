def p(g):
 for y in range(81):
  x=y%9;y//=9
  for j in g[y+2:][:len(s:={*g[y][x:x+2]+g[y+1][x:x+2]})*(s-{0,3}==s)]:j[x:x+2]=3,3
 return g