def p(g):
 a=str(g).count('5');r=[*map(list,g)]
 for k in range(100):u,v=k//10,k%10;x=g[u-a][v];r[u][v-a]=x*(x!=5)
 return r