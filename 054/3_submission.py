def p(g,R=range):
 s=sum(g,[]);b=s[0];a=max({*s}-{b},key=s.count);D=1,0,-1,0
 for z in R(676):
  i=z//26;j=z%26;q=sum(p:=[r[j:j+5]for r in g[i:i+5]],[])
  if{*q}-{a,b,q[12]}and p==[r[::-1]for r in p][::-1]:
   for r in g[i:i+5]:r[j:j+5]=[b]*5
   break
 for i,j in[(i,j)for i in R(30)for j in R(30)if a!=g[i][j]!=b]:
  for t in R(25):
   c=q[t];x=i+t//5-2;y=j+t%5-2
   if g[x][y]!=b!=c:g[x][y]=c
  for d in R(4):
   x=i+D[d]*2;y=j+D[d-3]*2;c=g[x][y]
   if a!=c!=b:
    while g[x][y]-b:g[x][y]=c;x+=D[d];y+=D[d-3]
 return g
