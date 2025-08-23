def p(g):
 h=len(g);w=len(g[0]);a,b={*sum(g,[])}-{0,8};d=0,1,0,-1;z=9**6
 while z:
  z-=1;r,q=z%97%h,z%89%w;i,j=r+d[z%4-1],q+d[z%4]
  if g[r][q]<1<w>j>-1<i<h and (c:=g[i][j])%8:g[r][q]=c^a^b
 return g