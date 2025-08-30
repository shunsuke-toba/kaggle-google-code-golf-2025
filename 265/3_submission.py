def p(g):
 q=g[0]*1
 for a,b in zip(g,g[1:]):
  p,q=q,b*1
  for j in range(17):
   if(sum(p[j:j+2]+q[j:j+2])<1)*(j%16<1or p[j-1]+q[j-1]|p[j+2]*q[j+2]-25):a[j:j+2]=b[j:j+2]=2,2
 return g