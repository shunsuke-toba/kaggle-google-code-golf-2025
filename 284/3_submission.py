def p(g):
 (a,b,c),(d,e,f)=[(i,j,v)for i,r in enumerate(g)for j,v in enumerate(r)if v]
 if b==e:
  t=(d-a-2)//2
  for r in g[a:a+t+1]:r[b]=c
  for r in g[d-t:d+1]:r[e]=f
  g[a+t][b-2:b+3]=[c]*5;g[d-t][e-2:e+3]=[f]*5
  for k in(-2,2):g[a+t+1][b+k]=c;g[d-t-1][e+k]=f
 else:
  t=(e-b-2)//2;B=b+t;E=e-t;r=g[a];r[b:B+1]=[c]*-~t;r=g[d];r[E:e+1]=[f]*-~t
  for k in range(-2,3):g[a+k][B]=c;g[d+k][E]=f
  for k in(-2,2):g[a+k][B+1]=c;g[d+k][E-1]=f
 return g
