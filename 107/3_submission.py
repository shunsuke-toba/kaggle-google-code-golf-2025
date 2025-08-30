def p(g):
 n=len({*g[4]})+1;a=g[0][1]<1;b=g[a][0]<1;r=range(5*n);return[[g[i//n][j//n]or 2*((i//n-a)&-2 and(i-j==(a-b)*n or i+j==(a+b+2)*n-1))for j in r]for i in r]