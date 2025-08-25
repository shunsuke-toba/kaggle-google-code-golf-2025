def p(g):i=sum(g,[]).index(0);return[g[~i//16-k][~i&15::-1][:3]for k in(0,1,2)]
