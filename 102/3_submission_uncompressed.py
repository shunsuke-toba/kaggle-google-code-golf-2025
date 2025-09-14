R=range(12);s=sum
def p(g):
 for i in R:
  for j in R:
   for k in R:
    u=g[i:i+k+2];v=u[1:-1]
    if 20*-~k-s(s(r[j:j+k+2])for r in u)<1>s(s(r[j+1:j+k+1])for r in v):
     for r in v:r[j+1:j+k+1]=[2]*k
 return g