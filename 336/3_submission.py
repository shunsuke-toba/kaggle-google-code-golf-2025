def p(g):
 s=sum(g,[]);a,b=divmod(s.index(5),10);c,d=divmod(99-s[::-1].index(5),10)
 for r in g[a+1:c]:r[b+1:d]=[8]*~(b-d)
 u,v=(g[c][5]<1)-(g[a][5]<1),(g[5][d]<1)-(g[5][b]<1);a=[a,5,c][u+1];b=[b,5,d][v+1]
 while b<10>a>-1<b:g[a][b]=8;a+=u;b+=v
 return g