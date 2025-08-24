def p(g):
 s=sum(g,[]);a,b=divmod(s.index(5),10);c,d=divmod(99-s[::-1].index(5),10)
 for r in g[a+1:c]:r[b+1:d]=[8]*~(b-d)
 u=(g[a][5]-g[c][5])//5;v=(g[5][b]-g[5][d])//5;a=[5,c,a][u];b=[5,d,b][v]
 while b<10>a>-1<b:g[a][b]=8;a+=u;b+=v
 return g