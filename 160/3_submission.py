def p(g):
 for z in range(64):
  a,b,c,*_=g[z>>3:];s=slice(z%8,z%8+3)
  if(a[s]+b[s]+c[s]).count(0)<2:a[s]=c[s]=0,2,0;b[s]=2,2,2
 return g