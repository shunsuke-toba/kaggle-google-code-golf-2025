def p(g):
 for k in 1,2:
  i=sum(g,[]).index(k);r=i//10;d=r-i%10
  while r<10>r-d>-1<r:g[r][r-d]=k;r+=2*k-3
 return g