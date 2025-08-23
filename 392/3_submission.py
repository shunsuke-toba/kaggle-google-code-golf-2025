def p(g,R=range):
 n=len(g);v=max(sum(g,[]))
 def D(r,c,t,m,b=0):
  o=[[b]*40 for _ in[0]*40]
  for i in R(m):
   s=(t+1)*i;A=r-s+t;B=r+s;C=c-s+t;E=c+s
   for y in R(A,B):o[y][C]=o[y][E-1]=v
   for x in R(C,E):o[A][x]=o[B-1][x]=v
  return[o[i][:n]for i in R(n)]
 return next(D(r,c,t,n,5)for k in R(n)for r,c in((k,0),(0,k))for t in(1,2)for m in(3,4)if D(r,c,t,m)==g)
