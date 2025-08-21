def p(g):
 n=len(g)//2;m=n+1;a=sum(g,[]);s,t=divmod(a.index(min(a,key=a.count)),2*n+1);s=(s>n)*m;t=(t>n)*m;return[r[t:t+n]for r in g[s:s+n]]
