def p(g):
 for k in range(9**5):
  H,W=len(g),len(g[0]);D=(-1,0,1,0);r,c,s=k%97%H,k%89%W,k%4;x,y=D[s],D[s-3];t=g[r][c]
  try:
   if([g[r+D[s-i-1]][c+D[s-i]]for i in(0,1,2,3)]==[5,0,0,5])*t>4:g[r+D[s-1]+x-H][c+x+y]=4
  except:0
  if H>r+x>-1<c+y<W>5>t:g[r+x][c+y]|=t
 return g