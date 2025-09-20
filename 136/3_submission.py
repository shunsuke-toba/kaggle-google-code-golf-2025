def p(g):
 for k in-1,1:
  i=sum(g,[]).index(k%3);r=i//10;i%=10
  while r<10>i>-1<r:g[r][i]=k%3;r-=k;i-=k
 return g