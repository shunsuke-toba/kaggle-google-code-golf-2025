def p(g,k=99):
 f=lambda i,j,t=0:-1<i<10>j>-1<g[i][j]-5<4+t and(g[i].__setitem__(j,t or 9)or f(i+1,j,t)+f(i-1,j,t)+f(i,j+1,t)+f(i,j-1,t)+1)
 while~k:f(k//10,k%10,5-f(k//10,k%10));k-=1
 return g
