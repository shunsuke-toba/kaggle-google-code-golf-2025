def p(g):
 for r in range(81):
  c=r%9;r//=9;v=g[r][c:c+2]+g[r+1][c:c+2];p=v.index(0)
  while(s:=sorted(v)[1])and(c:=c-1+p%2*2)>-1<(r:=r-1+(p&2))<9>c:g[r+p//2][c+p%2]=s
 return g