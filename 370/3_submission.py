def p(g):
 w=len(g[0]);b=g[0][0];Z=[]
 for k,v in enumerate(sum(g,[])):
  z=k//w+1j*(k%w)
  if v<1:Z+=z,
  elif v-b:P=z;D=v
 s=P-max(Z,key=lambda z:(abs((z:=P-z).real),abs(z.imag)))
 for _ in[0]*w+g:
  Z=[z+s for z in Z]
  for z in Z:
   if len(g)>z.real>=0<=z.imag<w:g[int(z.real)][int(z.imag)]=D
 return g

