def p(g,R=range):
 s=sum(g,[]);b=s[0];a=max({*s}-{b},key=s.count);D=1,0,-1,0
 for z in R(676):
  i,j=z//26,z%26;q=sum(p:=[r[j:j+5]for r in g[i:i+5]],[])
  if{*q}-{b,a,q[12]}and p==p[::-1]==[r[::-1]for r in p]:
   for r in g[i:i+5]:r[j:j+5]=[b]*5
   p=q;break
 for z in R(676):
  i,j=z//26+2,z%26+2
  if g[i-1][j]==g[i][j-1]==a!=g[i][j]:
   for t in R(25):
    c=p[t];x=i+t//5-2;y=j+t%5-2
    if g[x][y]!=b!=c:g[x][y]=c
   for d in R(4):
    x,y=i+D[d]*2,j+D[d-3]*2;c=g[x][y]
    if a!=c!=b:
     while g[x][y]-b:g[x][y]=c;x+=D[d];y+=D[d-3]
 return g
