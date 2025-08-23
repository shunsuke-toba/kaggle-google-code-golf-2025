def p(g):
 w=len(g[0]);s=[*range(n:=w*len(g))];s=s[:w]+s[-w:]+s[::w]+s[w-1::w]
 for p in s:
  p%=n
  if (l:=g[p//w])[p%w]<1:l[p%w]=3;s+=p+1,p-1,p+w,p-w
 return eval(str(g).replace('0','2'))
