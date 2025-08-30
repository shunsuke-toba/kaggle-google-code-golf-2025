def p(g):
 for a,b,c,_ in zip(*[(i for i in range(100)if sum(g,[])[i])]*4):
  for r in g[a//10+1:c//10]:r[a%10+1:b%10]=[2]*(~a+b)
 return g