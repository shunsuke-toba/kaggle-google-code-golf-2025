def p(g,o=0):
 s=[divmod(sum(g,[]).index(2),len(g[0]))]
 for y,x in s:
  try:1/(y>=0<=x);v=g[y][x];g[y][x]=0/v;s+=((y-1,x),(y+1,x),(y,x-1),(y,x+1));o+=v<3
  except:0
 return[[o//5*8]]
