def p(g):
 b=eval(str(g));k=2
 while 1:
  B,i,j,k=max((sum([-2,0,1,0,0,0][b[i+d][j]]+(d*(0<=j+d<len(g[0]))and [-2,0,1,0,0,0][b[i][j+d]])for d in range(-r,r+1))-r/3,i,j,r)for r in[k,3]for i in range(r,len(g)-r)for j in range(len(g[0])))
  if B<1:return g
  for d in range(-k,k+1):
   for y,x in(i+d,j),(i,j+d):b[y][x]//=5;g[y][x]+=3*b[y][x]