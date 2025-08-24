def p(g):
 for k in 1,2:
  r,c=divmod(sum(g,[]).index(k),10)
  while r<10>c>-1<r:g[r][c]=k;r+=2*k-3;c+=2*k-3
 return g