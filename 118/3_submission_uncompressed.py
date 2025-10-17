def p(g):
 q=eval(str(g));n=2;p=range
 while 1:
  c,i,j,n=max((sum((-6,0,3,0,0,0)[q[i+d][j]]+(d and 0<=j+d<len(q[0]) and(-6,0,3,0,0,0)[q[i][j+d]])for d in p(-n,n+1))-n,i,j,n)for n in p(n,4)for i in p(n,len(q)-n)for j in p(len(q[0])))
  if c<3:return g
  for d in p(-n,n+1):
   q[i+d][j]//=5;g[i+d][j]+=q[i+d][j]*3;q[i][j+d]//=5;g[i][j+d]+=q[i][j+d]*3