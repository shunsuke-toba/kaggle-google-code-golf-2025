R=range
def p(g):
 s=[]
 while g:
  c=g[0][0];s+=c,
  while g and {c}=={*g[0]}:g=g[1:]
  while g and {c}=={*g[-1]}:g=g[:-1]
  while g and {c}=={r[0]for r in g}:g=[r[1:]for r in g]
  while g and {c}=={r[-1]for r in g}:g=[r[:-1]for r in g]
 m=len(s)*2-1
 return [[s[min(i,j,m-1-i,m-1-j)]for j in R(m)]for i in R(m)]
