def p(g):
 for r in range(81):
  c=r%9;r//=9;v=g[r][c:c+2]+g[r+1][c:c+2]
  if v.count(0)<2:
   p=v.index(0);r+=p//2*3-1;c+=p%2*3-1
   while-1<r<10>c>-1:g[r][c]=v[~p];r+=p//2*2-1;c+=p%2*2-1
 return g