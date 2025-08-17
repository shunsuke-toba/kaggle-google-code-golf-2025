def p(g):
 h,w,r=len(g),len(g[0]),range
 for s in r(min(h,w),0,-1):
  for i in r(1,h-s):
   for j in r(1,w-s):
    if all(g[i-1][k]==g[i+s][k]==5 for k in r(j,j+s))and all(g[k][j-1]==g[k][j+s]==5>max(g[k][j:j+s])+4 for k in r(i,i+s)):
     for v in g[i:i+s]:v[j:j+s]=[2]*s
 return g
