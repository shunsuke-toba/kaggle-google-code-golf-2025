def p(g):
 a=sum(g,[]);i=a.index(8);g=[10*[0]for _ in g];j=-1
 for v in a:j+=1;g[i//10+(j>i)][i%10+(j%10>i%10)]+=v*(v!=8)
 return g