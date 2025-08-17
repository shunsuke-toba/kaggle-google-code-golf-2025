def p(g):
 s=sum(g,[]);t,l=divmod(s.index(5),10);b,d=divmod(99-s[::-1].index(5),10)
 for r in g[t+1:b]:r[l+1:d]=[8]*~(l-d)
 i,j=next((i,j)for i in range(t,b+1)for j in range(l,d+1)if not g[i][j]);u=(i==b)-(i==t);v=(j==d)-(j==l)
 while 10>i>-1<j<10:g[i][j]=8;i+=u;j+=v
 return g