def p(g):
 for k in range(9**5):
  H,W=len(g),len(g[0]);D=(-1,0,1,0);r,c,s=k%97%H,k%89%W,k%4;x,y=D[s],D[s-3];u,v,t,a,b=r+D[s-1]+x,c+x+y,g[r][c],r+x,c+y
  try:n=[g[r+D[i]][c+D[i-3]]for i in(0,1,2,3)]*2
  except:n=D
  if(n[s:s+4]==[5,0,0,5])*t>4<H>u>-1<v<W:g[u][v]=4
  if H>a>-1<b<W>5>g[a][b]>t:g[r][c]=4
 return g