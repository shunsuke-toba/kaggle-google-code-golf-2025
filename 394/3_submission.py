def p(g):n=len(g);a=sum(g,[]).index(0);r=a//n;t=3-(n<7);w=g[r].count(0);return[g[i+(i<t)*2*t-t][a%n:a%n+w]for i in range(r,r+w)]
