def p(g):
 a=sum(g,[]);b=max(a,key=a.count);z=[];h=len(g);w=len(g[0])
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v<1:z+=i+1j*j,
   elif v!=b:D=v;p=i+1j*j
 c=sum(z)/len(z)
 s=complex((p.real>c.real)*2-1,(p.imag>c.imag)*2-1)
 k=1
 while set(z)&{x+k*s for x in z}:k+=1
 s*=k
 while 1:
  z=[x+s for x in z];f=0
  for x in z:
   i=int(x.real);j=int(x.imag)
   if 0<=i<h and 0<=j<w:g[i][j]=D;f=1
  if not f:break
 return g
