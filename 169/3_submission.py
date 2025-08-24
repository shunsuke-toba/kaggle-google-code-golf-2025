def p(g,k=99):
 f=lambda i,j,c=9:-1<i<10>j>-1<4<g[i][j]<9+c%9 and(g[i].__setitem__(j,c)or f(i+1,j,c)+f(i-1,j,c)+f(i,j+1,c)+f(i,j-1,c)+1)
 while~k:f(k//10,k%10,5-f(k//10,k%10));k-=1
 return g
