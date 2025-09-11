def p(g):
 for k in 1,2:
  i=sum(g,[]).index(k);r=i//10;i-=r*11
  while r<10>r+i>-1<r:g[r][r+i]=k;r+=2*k-3
 return g