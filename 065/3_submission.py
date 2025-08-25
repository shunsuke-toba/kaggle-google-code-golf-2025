def p(g):m=len(g);n=m//2;f=sum(g,[]);i=f.index(min(f,key=f.count));d=-~n;return[r[d*(i%m>n):][:n]for r in g[d*(i//m>n):][:n]]
