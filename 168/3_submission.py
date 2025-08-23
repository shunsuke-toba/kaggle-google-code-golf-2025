def p(g):
 for r in range(81):
  c=r%9;r//=9;v=g[r][c:c+2]+g[r+1][c:c+2]
  if v.count(0)==1:
   p=v.index(0);a=(p&2)-1;b=p%2*2-1;r+=a+p//2;c+=b+p%2
   while-1<r<10>c>-1:g[r][c]=v[p-1];r+=a;c+=b
 return g
