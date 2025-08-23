def p(g):
 w=len(g[0]);n=w*len(g);r=range;s=[*r(w),*r(n-w,n),*r(0,n,w),*r(w-1,n,w)]
 for p in s:
  i,j=divmod(p%n,w)
  if g[i][j]<1:g[i][j]=3;s+=p+1,p-1,p+w,p-w
 return eval(str(g).replace('0','2'))
