def p(g):
 R=range;h=len(g)-6
 for z in R(h**2):
  y,x=divmod(z,h)
  if g[y][x]==g[y][x+1]==g[y+1][x]==5 and(t:={(i,j)for i in R(5)for j in R(5)if(v:=g[y+i+1][x+j+1])>1 and(c:=v)}):break
 for z in R((h+2)**2):
  y,x=divmod(z,h+2)
  if {(i,j)for i in R(5)for j in R(5)if g[y+i][x+j]==1}==t:
   for i,j in t:g[y+i][x+j]=c
 return g
