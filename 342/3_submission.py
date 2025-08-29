def p(g):
 a=sum(g,[]);i,j=a.index(8),0;g=[10*[0]for _ in g]
 for v in a:g[i//10+(j>i)][i%10+(j%10>i%10)]+=v*(v!=8);j+=1
 return g