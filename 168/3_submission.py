def p(g):
 for r in range(81):
  c=r%9;r//=9
  if s:=sorted(v:=g[r][c:c+2]+g[r+1][c:c+2])[1]:
   p=v.index(0);r+=p>1;c+=p&1
   while(c:=c-1+p%2*2)>-1<(r:=r-1+(p&2))<10>c:g[r][c]=s
 return g