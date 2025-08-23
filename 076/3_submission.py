def p(g):
 L=len;R=range;E=enumerate;W=L(g[0]);y,x=next((i//W,i%W)for i,v in E(sum(g,[]))if v&1)
 a=[*map(list,g)];S=[(y,x)];a[y][x]=0
 for y,x in S:
  for Y in R(y-1,y+2):
   for X in R(x-1,x+2):
    if L(g)>Y>=0<=X<W and a[Y][X]:a[Y][X]=0;S+=(Y,X),
 c,d=zip(*S);t=[r[min(d):max(d)+1]for r in g[min(c):max(c)+1]]
 for _ in R(8):
  for y in R(L(g)+1-L(t)):
   for x in R(W+1-L(t[0])):
    if all(g[y+i][x+j]==u for i,r in E(t)for j,u in E(r)if u&1<1<u):
     for i,r in E(t):
      for j,u in E(r):g[y+i][x+j]|=u
  t=[*zip(*t[::-1])];3==_ and t.reverse()
 return g
