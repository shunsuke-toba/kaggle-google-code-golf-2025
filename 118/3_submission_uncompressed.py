def p(g):
 b=eval(str(g));k=2
 while 1:
  B,i,j,k=max((sum((-6,0,3,0,0,0)[b[i+d][j]]+(d*(0<=j+d<len(g[0]))and(-6,0,3,0,0,0)[b[i][j+d]])for d in range(-r,r+1))-r,i,j,r)for r in(k,3)for i in range(r,len(g)-r)for j in range(len(g[0])))
  if B<3:return g
  for d in range(-k,k+1):
   b[i+d][j]//=5;g[i+d][j]+=3*b[i+d][j];b[i][j+d]//=5;g[i][j+d]+=3*b[i][j+d]