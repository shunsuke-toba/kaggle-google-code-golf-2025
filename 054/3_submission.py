def p(g,R=range):
 C=sorted({*(s:=sum(g,[]))},key=s.count);D=1,0,-1,0;b,a=g[0][0],C[-1]
 if C[-1]==b:a=C[-2]
 for z in R(676):
  i,j=z//26,z%26
  p=[g[k][j:j+5]for k in R(i,i+5)]
  if len({*sum(p,[])}|{b}|{a})>=4 and p[::-1]==p and [r[::-1]for r in p]==p:
   for k in R(5):g[i+k][j:j+5]=[b]*5
   break
 for z in R(676):
  i,j=z//26+2,z%26+2
  if b!=g[i][j]==p[2][2]!=a==g[i][j-1]==g[i-1][j]:
   for t in R(25):
    k,l=t//5,t%5
    if g[i+k-2][j+l-2]!=b!=p[k][l]!=a:g[i+k-2][j+l-2]=p[k][l]
   for d in R(4):
    x,y=i+D[d]*2,j+D[d-3]*2
    if a!=(c:=g[x][y])!=b:
     while g[x][y]!=b:g[x][y]=c;x+=D[d];y+=D[d-3]
 return g
