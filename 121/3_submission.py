def p(g):f=sum(g,[]);i=f.index(8);g=[f[j:j+3]for j in(i-14,i-1,i+12)];g[1][1]=sum({*sum(g,[])})-8;return g
