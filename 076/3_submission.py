def p(g):
 L=len;R=range;E=enumerate;H,W=L(g),L(g[0]);i=next(i for i,v in E(sum(g,[]))if v&1);S=[divmod(i,W)]
 for y,x in S:
  for Y in R(y-1,y+2):
   for X in R(x-1,x+2):
    if H>Y>=0<=X<W and g[Y][X]and(Y,X)not in S:S+=(Y,X),
 r,c=zip(*S);t=[row[min(c):max(c)+1]for row in g[min(r):max(r)+1]]
 for _ in R(8):
  for y in R(H-L(t)+1):
   for x in R(W-L(t[0])+1):
    if all(g[y+i][x+j]==u for i,r in E(t)for j,u in E(r)if u&1<1<u):
     for i,r in E(t):
      for j,u in E(r):g[y+i][x+j]|=u
  t=[*zip(*t[::-1])];3==_ and t.reverse()
 return g

