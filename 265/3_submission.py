def p(g):
 a=g[0];p=a[:]
 for b in g[1:]:
  q=b[:]
  for j in range(17):
   if(sum(p[j:j+2]+q[j:j+2])<1)*(j%16<1or p[j-1]+q[j-1]|p[j+2]*q[j+2]-25):a[j:j+2]=b[j:j+2]=2,2
  a=b;p=q
 return g