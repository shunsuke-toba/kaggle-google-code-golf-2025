def p(g):i=sum(g,[]).index(0);c=~i&15;return[g[~i//16-k][c:c-3:-1]for k in(0,1,2)]
