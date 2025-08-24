def p(g):
 for z in range(64):
  a,b,c=g[z>>3:][:3];x=z%8
  if sum(a[x:x+3]+b[x:x+3]+c[x:x+3])-b[x+1]==8:a[x:x+3]=c[x:x+3]=0,2,0;b[x:x+3]=2,2,2
 return g