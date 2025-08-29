def p(g):
 t=81
 while t:
  t-=1;x=t%9;y=t//9
  for j in g[y+2:][:len(s:={*g[y][x:x+2]+g[y+1][x:x+2]})*(min(s)>0)]:j[x:x+2]=3,3
 return g