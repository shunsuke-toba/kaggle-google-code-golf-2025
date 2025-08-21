def p(g):
 t=lambda z:list(map(list,zip(*z)));R=range;n=len(g)
 x,y=zip(*[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v])
 a=min(x);b=max(x);c=min(y);d=max(y)
 if 0 in g[a][c+2:d-1]:o=0
 elif 0 in g[b][c+2:d-1]:o=1
 elif 0 in(r[c]for r in g[a+2:b-1]):o=2
 else:o=3
 if o==1:g=g[::-1];a,b=n-1-b,n-1-a
 elif o==2:g=t(g);a,b,c,d=c,d,a,b
 elif o==3:g=t(g)[::-1];a,b,c,d=n-1-d,n-1-c,a,b
 h=[r[:]for r in g]
 for i in R(a+1,b):h[i][c+1:d]=[4]*(d-c-1)
 for i in R(b):h[i][c+2:d-1]=[4]*(d-c-3)
 for k in R(a):
  i=a-1-k;L=c+1-k;R=d-1+k
  if L>=0:h[i][L]=4
  if R<n:h[i][R]=4
 return[h,h[::-1],t(h),t(h[::-1])][o]
