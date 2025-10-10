def p(g):
 c=eval(str(g));k=2
 while 1:
  b,i,j,k=max((sum((-6,0,3,0,0,0)[c[i+d][j]]+(d and 0<=j+d<len(g[0]) and(-6,0,3,0,0,0)[c[i][j+d]])for d in range(-r,r+1))-r,i,j,r)for r in(k,3)for i in range(r,len(g)-r)for j in range(len(g[0])))
  if b<3:return g
  for d in range(-k,k+1):
   c[i+d][j]//=5;g[i+d][j]+=c[i+d][j]*3;c[i][j+d]//=5;g[i][j+d]+=c[i][j+d]*3