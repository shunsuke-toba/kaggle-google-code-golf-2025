def p(g):m=len(g);n=m//2;b=sum(g,[]);i=b.index(min(b,key=b.count));s,t=(i//m>n)*-~n,(i%m>n)*-~n;return[r[t:t+n]for r in g[s:s+n]]
