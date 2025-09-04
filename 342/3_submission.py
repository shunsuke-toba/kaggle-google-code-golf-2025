def p(g):
 a=sum(g,[]);i=k=a.index(8);g=[10*[0]for _ in g]
 for v in a:g[k//10+(i<0)][k%10+(i%10>k%10)]+=v*(v!=8);i-=1
 return g