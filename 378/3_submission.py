def p(g):
 n=len(g)-1
 for i in range(1,n):
  for j in range(1,n):
   if(c:=g[i][j])and(d:=(g[i+1][j]==c)-(g[i-1][j]==c))*(e:=(g[i][j+1]==c)-(g[i][j-1]==c))and g[i+d][j+e]^c:
    y,x=i,j;k=g[i+2*d][j+2*e]
    while 0<y<n>0<x<n:g[y:=y-d][x:=x-e]=k
 return g
