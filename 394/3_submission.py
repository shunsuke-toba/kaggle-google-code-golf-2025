def p(g):n=len(g);x=sum(g,[]);a=x.index(0);b=n*n+~x[::-1].index(0);t=3-(n<7);return[g[i+(i<t)*2*t-t][a%n:b%n+1]for i in range(a//n,b//n+1)]
