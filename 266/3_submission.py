def p(g):
 i=sum(g,[]).index(2)
 for j,c in(i-6,3),(i-4,6),(i+4,8),(i+6,7),(i,0):
  if-1<j<15>-2<j%5-i%5<2:g[j//5][j%5]=c
 return g