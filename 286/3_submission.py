def p(g):
 h=len(g);w=len(g[0]);a,b={*sum(g,[])}-{0,8};d=0,1,0,-1;z=7**7
 while z:=z-1:
  if g[r:=z%97%h][q:=z%89%w]<1<w>(j:=q+d[z%4])>-1<(i:=r+d[~z%4])<h>(k:=g[i][j])%8>0:g[r][q]=k^a^b
 return g