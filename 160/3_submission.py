def p(g):
 for y in range(len(g)-2):
  a,b,c=g[y:y+3]
  for x in range(len(b)-2):
   if b[x+1]<1 and sum(a[x:x+3]+b[x:x+3]+c[x:x+3])>7:a[x+1]=c[x+1]=b[x+1]=b[x]=b[x+2]=2;a[x]=a[x+2]=c[x]=c[x+2]=0
 return g
