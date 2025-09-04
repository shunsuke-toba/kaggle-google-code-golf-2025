def p(g):
 R=range;F=-2,0,1,0,0,0;b=eval(str(g));h,w=len(g),len(g[0]);k=2
 while 1:
  B,i,j,k=max((sum((0<=i+d<h and F[b[i+d][j]])+(d*(0<=j+d<w) and F[b[i][j+d]])for d in R(-r,r+1))-r//3,i,j,r)for i in R(h)for j in R(w)for r in(k,3))
  if B<1:return g
  for d in R(-k,k+1):
   for y,x in(i+d,j),(i,j+d):g[y][x]+=b[y][x]//5*3;b[y][x]=0