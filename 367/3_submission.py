def p(g):
 H,W=len(g),len(g[0]);D=(-1,0,1,0)
 for k in range(9999):
  r,c,s=k//(W*4)%H,k//4%W,k%4
  try:n=[g[r+D[i]][c+D[i-3]]for i in(0,1,2,3)]*2
  except:n=D
  u,v,t=r+D[s-1]+D[s],c+D[s]+D[s-3],g[r][c]
  if(n[s:s+4]==[5,0,0,5])*t>4<H>u>-1<v<W:g[u][v]=4
  a,b=r+D[s],c+D[s-3]
  if H>a>-1<b<W>5>g[a][b]>t:g[r][c]=4
 return g