def p(g,R=range):
 h,w=len(g),len(g[0])
 for d in 0,1:
  H,W=(h,w)if d else(w,h)
  for k in R(H):
   c=sum(1 for j in R(W) if(g[k][j] if d else g[j][k]))
   for m in R(2*W):
    y=2*W-1-m;j,x=(m,m-c)if m<W else(y,y+c)
    if 1<c<W>x>=0<(v:=g[k][x] if d else g[x][k]):(g[k] if d else g[j])[j if d else k]=v
 return g