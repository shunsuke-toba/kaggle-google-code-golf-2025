def p(g):
 h=len(g);w=len(g[0])
 a=sum(g,[]);b=max(a,key=a.count)
 Z=[]
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v<1:Z+=i+1j*j,
   elif v!=b:P=i+1j*j;D=v
 s=P-max(Z,key=lambda x:(abs((P-x).real),abs((P-x).imag)))
 while 1:
  Z=[z+s for z in Z];f=0
  for z in Z:
   i=int(z.real);j=int(z.imag)
   if h>i>=0<=j<w:g[i][j]=D;f=1
  if not f:break
 return g
