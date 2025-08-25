def p(g):
 e=enumerate;t=lambda x:[*map(list,zip(*x))]
 if not(L:=[i for i,r in e(g)if r[0]]):return t(p(t(g)))
 for k,j,l in((i,j,l)for l in L for i,r in e(g)for j,v in e(r)if v&2):
  while g[k][j]^8 and k-l:g[k][j]=2;k+=k<l or-1
  if k==l:
   for m in-1,0,1:g[l+m][j-1:j+2]=8,8,8;g[l][j]=2
 return g