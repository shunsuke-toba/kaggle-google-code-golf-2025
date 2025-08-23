def p(g,R=range):
 n=len(g);f=max(sum(g,[]));O=25
 def d(r,c,t,m,b):
  o=[[b]*64 for _ in[0]*64]
  r+=O;c+=O
  for i in R(m):
   s=(t+1)*i;A=r-s+t;B=r+s;C=c-s+t;E=c+s
   for y in R(A,B):o[y][C]=o[y][E-1]=f
   for x in R(C,E):o[A][x]=o[B-1][x]=f
  return [r[O:O+n]for r in o[O:O+n]]
 for k in R(n):
  for r,c in(k,0),(0,k):
   for t in 1,2:
    for s in 2,3:
     if d(r,c,t,s+1,0)==g:return d(r,c,t,n,5)

