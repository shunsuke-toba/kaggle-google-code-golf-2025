def p(g):
 R,C=len(g),len(g[0])
 for i in range(R):
  for j in range(C):
   if g[i][j]==5:m=(i,j)
 mr,mc=m
 b,M=None,0
 for t in range(R-2):
  for l in range(C-2):
   p=[]
   n=0
   for i in range(t,t+3):
    for j in range(l,l+3):
     v=g[i][j]
     p.append(v)
     n+=v!=0
   if n>M:M,b=n,p
 s=mr-1
 t=mc-1
 for i in range(3):
  for j in range(3):
   nr,nc=s+i,t+j
   g[nr][nc]=b[i*3+j]
 return g