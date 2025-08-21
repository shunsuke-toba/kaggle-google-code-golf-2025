def p(g):
 n,m=len(g)-1,len(g[0])-1
 for i in range(1,n):
  for j in range(1,m):
   if(c:=g[i][j]):
    d=(g[i+1][j]==c)-(g[i-1][j]==c);e=(g[i][j+1]==c)-(g[i][j-1]==c)
    if d*e and g[i+d][j+e]^c:
     y,x=i,j
     while 0<y<n>0<x<m:y-=d;x-=e;g[y][x]=g[i+2*d][j+2*e]
 return g
