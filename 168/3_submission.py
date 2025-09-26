def p(g):
 for r in range(81):
  v=g[q:=r//9][(c:=r%9):c+2]+g[q+1][c:c+2];p=v.index(0)
  while(s:=sorted(v)[1])and(c:=c-1+p%2*2)>-1<(q:=q-1+(p&2))<9>c:g[q+p//2][c+p%2]=s
 return g