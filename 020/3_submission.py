def p(g):
 f=lambda h:[*map(any,h)].index(1);m=f(g);n=f(zip(*g));k=75
 while k:k-=1;i=k//5%5;g[m+i][n+k%5]|=g[m+~k%5][n+i]
 return g