def p(g):
 g=[r[:]for r in g];h,w=len(g),len(g[0])
 for y in range(h-1):
  for x in range(w-1):
   if all(g[y+i][x+j]for i in(0,1)for j in(0,1)):
    v=[g[y+i][x+j]for i in(0,1)for j in(0,1)]
    if 2 in v:
     c=[i for i in v if i-2][0]
     for k in range(4):
      if v[k]==2:
       i,j=y+k//2,x+k%2;a,b=k//2*2-1,k%2*2-1
       while-1<i<h and-1<j<w:g[i][j]=c;-1<i+a<h and exec('g[i+a][j]=c');-1<j+b<w and exec('g[i][j+b]=c');i+=a;j+=b
     return g
 return g