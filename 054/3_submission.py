def p(g,R=range):
 s=sum(g,[]);b=s[0];a=max({*s}-{b},key=s.count);D=1,0,-1,0
 for z in R(676):
  i,j=z//26,z%26;p=[r[j:j+5]for r in g[i:i+5]]
  if{*sum(p,[])}-{b,a,p[2][2]}and p==p[::-1]==[r[::-1]for r in p]:
   for r in g[i:i+5]:r[j:j+5]=[b]*5
   break
 for z in R(676):
  i,j=z//26+2,z%26+2
  if g[i-1][j]==g[i][j-1]==a!=g[i][j]:
   for t in R(25):
    k,l=divmod(t,5);c=p[k][l]
    if g[i+k-2][j+l-2]!=b!=c!=a:g[i+k-2][j+l-2]=c
   for d in R(4):
    x,y=i+D[d]*2,j+D[d-3]*2;c=g[x][y]
    if a!=c!=b:
     while g[x][y]!=b:g[x][y]=c;x+=D[d];y+=D[d-3]
 return g
