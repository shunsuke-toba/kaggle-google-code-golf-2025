def p(g):
 h=len(g);w=len(g[0]);t=[*{*sum(g,[])}-{0,8}];d=1,0,-1,0
 for z in range(9**6):
  r,q=z%97%h,z%89%w;i,j=r+d[z%4],q+d[z%4-3]
  if h>i>-1<j<w and g[r][q]-8 and (c:=g[i][j])%8:g[r][q]=t[c==t[0]]
 return g