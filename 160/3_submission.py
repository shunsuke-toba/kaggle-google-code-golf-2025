def p(g):
 for z in range(64):
  a,b,c=g[z>>3:][:3];x=z%8;s=slice(x,x+3)
  if sum(a[s]+b[s]+c[s])-b[x+1]>7:a[s]=c[s]=0,2,0;b[s]=2,2,2
 return g
