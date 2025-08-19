def p(g,R=range):
 n=len(g);s=[x[:]for x in g]
 for i in R(n):
  for j in R(n):
   if 8<g[i][j]and(i<1or g[i-1][j]-9)*(j<1or g[i][j-1]-9):
    a=c=0
    while j+a<n>g[i][j+a]>8:a+=1
    while i+c<n>g[i+c][j]>8:c+=1
    for x in R(j,j+a):
     y=i+c
     while y<n>s[y][x]<1:g[y][x]=1;y+=1
    r=max(a,c)//2;t=max(0,i-r);b=min(n,i+c+r);l=max(0,j-r);e=min(n,j+a+r)
    for y in R(t,b):g[y][l:e]=[(9,3)[v<9]for v in g[y][l:e]]
 return g