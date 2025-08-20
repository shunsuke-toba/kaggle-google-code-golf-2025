def p(g):
 for n in range(81):
  y=n//9;x=n%9;s={*g[y][x:x+2]+g[y+1][x:x+2]}
  for j in g[y+2:][:len(s)*(s-{0,3}==s)]:j[x:x+2]=3,3
 return g
