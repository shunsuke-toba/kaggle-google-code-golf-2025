def p(g):
 L=len;V={};G=V.get;H,W=L(g),L(g[0]);N=lambda x,y:[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
 for k in range(H*W):
  r,c=k//W,k%W
  if g[r][c]|G((r,c),0):continue
  C=[];S=[(r,c)]
  while S:
   x,y=S.pop()
   if G((x,y)):continue
   V[x,y]=1;C+=(x,y),
   for i,j in N(x,y):
    if H>i>-1<j<W>1>g[i][j]==G((i,j),0):S+=(i,j),
  R=[p[0]for p in C];Q=[p[1]for p in C];a,b,c,d=min(R),max(R),min(Q),max(Q)
  for x,y,i,j in[(a,c,-1,-1),(a,d,-1,1),(b,c,1,-1),(b,d,1,1)]:
   u,v=x+i,y+j;s=sum(H>p>-1<q<W>g[p][q]>4for p,q in N(u,v))
   if s<3<H>u>-1<v<W>g[u][v]>4>0<L(C)==(b-a+1)*(d-c+1):
    for x,y in C:g[x][y]=4
 return g