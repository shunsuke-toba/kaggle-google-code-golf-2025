def p(g):
 w=len(g[0]);Z=[];k=0
 for v in sum(g,[]):
  z=k//w+k%w*1j;k+=1
  if v<1:Z+=z,
  elif v-g[0][0]:P=z;d=v
 P-=max(Z,key=lambda z:(abs((z:=P-z).real),abs(z.imag)))
 for _ in[0]*w+g:
  Z=[z+P for z in Z]
  for z in Z:
   if len(g)>z.real>-1<z.imag<w:g[int(z.real)][int(z.imag)]=d
 return g