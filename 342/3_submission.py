def p(g):
 a=sum(g,[]);r,c=divmod(a.index(8),10);g=[10*[0]for _ in g]
 for i,v in enumerate(a):g[r+(i//10>r)][c+(i%10>c)]+=v*(v!=8)
 return g
