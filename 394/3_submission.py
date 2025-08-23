def p(g):n=len(g);x=sum(g,[]);a=x.index(0);c=n*n+~x[::-1].index(0);t=2+(n>6);return[[g[i+(i<t)*2*t-t][j]for j in range(a%n,1+c%n)]for i in range(a//n,1+c//n)]
