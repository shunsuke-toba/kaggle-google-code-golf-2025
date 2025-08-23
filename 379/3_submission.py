def p(g):
 e=enumerate;t=lambda x:list(map(list,zip(*x)))
 L=[i for i,r in e(g) if{8}==set(r)]
 if not L:return t(p(t(g)))
 for i,j in((i,j)for i,r in e(g)for j,v in e(r)if v==2):
  for l in L:
   k=i
   while g[k][j]-8 and k-l:
    g[k][j]=2;k+=1-2*(l<k)
   if k==l:
    for m in l-1,l,l+1:g[m][j-1:j+2]=8,8,8;g[l][j]=2
 return g
