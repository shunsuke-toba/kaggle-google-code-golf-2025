def p(g):
 w=len(g[0]);n=w*len(g);s=[*range(w),*range(0,n,w)]
 for p in s:
  l=g[p%n//w];i=p%w
  if l[i]<1:l[i]=3;s+=p+1,p-1,p+w,p-w
 return eval(f'{g}'.replace(*'02'))
