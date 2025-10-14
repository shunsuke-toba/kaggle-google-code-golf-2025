def p(g):
 c=eval(str(g));k=2;r=range
 while 1:
  b,i,j,k=max((sum((-6,0,3,0,0,0)[c[i+d][j]]+(d and 0<=j+d<len(c[0]) and(-6,0,3,0,0,0)[c[i][j+d]])for d in r(-k,k+1))-k,i,j,k)for k in r(k,4)for i in r(k,len(c)-k)for j in r(len(c[0])))
  if b<3:return g
  for d in r(-k,k+1):
   c[i+d][j]//=5;g[i+d][j]+=c[i+d][j]*3;c[i][j+d]//=5;g[i][j+d]+=c[i][j+d]*3