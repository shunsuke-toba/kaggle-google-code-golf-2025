def p(g,z=64):
 while z:
  z-=1;a,b,c,*_=g[z>>3:];s=slice(z%8,z%8+3)
  if min(a[s]+c[s]):a[s]=c[s]=0,2,0;b[s]=2,2,2
 return g