def p(g):
 r=range;w=len(g[0]);h=len(g);s=[*r(w),*r(0,h*w,w)]
 for p in s:
  if(l:=g[p//w%h])[p%w]<1:l[p%w]=3;s+=p+1,p-1,p+w,p-w
 return eval(str(g).replace(*'02'))
