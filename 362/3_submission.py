def p(g):
 a=str(g).count('5');r=[*map(list,g)]
 for k in range(100):x=g[k//10][k%10];r[(k//10+a)%10][(k-a)%10]=x*(x!=5)
 return r