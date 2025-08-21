def p(g,R=range(11)):
 o=[[0]*3]*3
 for i in R:
  for j in R:
   if g[i][j]==5:o=[[*map(max,zip(o[x],g[i+x-1][j-1:j+2]))]for x in(0,1,2)]
 return o