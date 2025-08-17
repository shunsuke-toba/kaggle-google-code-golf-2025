def p(g):
 h=len(g);w=len(g[0]);r=range
 for y in r(h):
  for x in r(w):g[y][x]*=any(-1<i<h and -1<j<w and g[i][j]for i in r(y-1,y+2)for j in r(x-1,x+2)if i-y or j-x)
 return g
