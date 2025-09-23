def p(g):
 for _ in g*4:
  g=[*map(list,zip(*g[::-1]))];x=y=0
  for j in range(81):g[i:=j//9+1][j:=j%9]|=x*(i+j==y);x|=g[i][j];y|=(i+j)*(g[i-1][j]*g[i][j+1]*g[i-1][j+1]>0)
 return g