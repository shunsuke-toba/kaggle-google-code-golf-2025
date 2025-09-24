def p(g):
 a=sum(g,[]);k=a.index(8);j=0
 for v in a:g[j//10][j%10]-=v;g[k//10+(j>k)][k%10+(j%10>k%10)]+=v*(v!=8);j+=1
 return g