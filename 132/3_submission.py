def p(g,e=enumerate):
 o=[[0]*len(g[0])for _ in g]
 for k in {*sum(g,[])}-{0}:
  a,b=zip(*((i,j)for i,r in e(g)for j,x in e(r)if x==k))
  m,M=min(b),max(b)+1
  for i in range(min(a),-~max(a)):o[i][m:M]=[k]*(M-m)
 return o
