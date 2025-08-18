def p(g):
 for k in range(9**5):
  H,W=len(g),len(g[0]);D=(-1,0,1,0);r,c,s=k%97%H,k%89%W,k%4;x,y=D[s],D[s-3];u,v,t,a,b=r+D[s-1]+x,c+x+y,g[r][c],r+x,c+y
  try:
   if([g[r+D[s-i-1]][c+D[s-i]]for i in(0,1,2,3)]==[5,0,0,5])*t>4:g[u-H][v]=4
  except:0
  if H>a>-1<b<W>5>t:g[a][b]|=t
 return g