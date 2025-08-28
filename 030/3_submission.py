def p(g):
 b=sum(g,[]);f=b.index;g=[[0]*10for _ in g]
 for i,v in enumerate(b):
  if v:g[(i+f(1)-f(v))//10][i%10]=v
 return g