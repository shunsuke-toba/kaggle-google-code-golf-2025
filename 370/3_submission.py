def p(g):
 w=len(g[k:=0]);Z=[]
 for v in sum(g,[]):
  z=k//w+k%w*1j;k+=1
  if v<1:Z+=z,
  elif v-g[0][0]:p=z;d=v
 p-=max(Z,key=lambda z:abs((z:=p-z).real*w+1j*z.imag))
 for z in Z:
  while len(g)>(z:=z+p).real>~0<z.imag<w:g[int(z.real)][int(z.imag)]=d
 return g