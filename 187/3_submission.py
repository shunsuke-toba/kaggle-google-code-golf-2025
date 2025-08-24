def p(g):
 w=len(g[0]);n=w*len(g);s=[*range(w),*range(0,n,w)]
 for p in s:
  p%=n
  if(l:=g[p//w])[p%w]<1:l[p%w]=3;s+=p+1,p-1,p+w,p-w
 return eval(str(g).replace('0','2'))