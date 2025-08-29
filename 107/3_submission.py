def p(g):
 n=len({*g[4]})+1;a=g[0][1]<1;b=g[1][0]<1;R=range(5*n);return [[2 if (v:=g[i//n][j//n])<1 and (i//n-a)&-2 and (i-j==(a-b)*n or i+j==(a+b+2)*n-1) else v for j in R]for i in R]