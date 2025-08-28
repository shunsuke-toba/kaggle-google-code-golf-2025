def p(g):
 s=[i for i in range(100)if sum(g,[])[i]]
 while s:
  a,b,c,_,*s=s
  for r in g[a//10+1:c//10]:r[a%10+1:b%10]=[2]*(~a+b)
 return g