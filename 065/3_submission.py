def p(g):n=len(g)//2;b=sum(g,[]);s,t=divmod(b.index(min(b,key=b.count)),2*n+1);s=(s>n)*-~n;t=(t>n)*-~n;return[r[t:t+n]for r in g[s:s+n]]
