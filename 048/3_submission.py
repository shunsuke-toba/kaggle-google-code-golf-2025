def p(g,o=0):
 s=[divmod(sum(g,[]).index(2),len(g[0]))]
 while s:
  y,x=s.pop()
  try:1/(y|x>=0);v=g[y][x];g[y][x]=0/v;(s.extend(((y-1,x),(y+1,x),(y,x-1),(y,x+1))),o:=o+(v<3))
  except:0
 return[[o//5*8]]