def p(g):
 L=len;r,e=range,enumerate;H=L(g);W=L(g[0])
 s=sum(g,[]);k=next(i for i,v in e(s) if v%2)
 y,x=divmod(k,W);a=[*map(list,g)];S=[(y,x)];a[y][x]=0;c=d=()
 while S:
  i,j=S.pop();c+=i,;d+=j,
  for Y in r(i-1,i+2):
   for X in r(j-1,j+2):
    if H>Y>=0<=X<W and a[Y][X]:a[Y][X]=0;S+=(Y,X),
 t=[q[min(d):max(d)+1]for q in g[min(c):max(c)+1]]
 for _ in r(8):
  for y in r(H+1-L(t)):
   for x in r(W+1-L(t[0])):
    if all(g[y+i][x+j]==u for i,R in e(t) for j,u in e(R) if u&1<1<u):
     for i,R in e(t):
      for j,u in e(R):g[y+i][x+j]|=u
  t=[*zip(*t[::-1])]
  if _==3:t=t[::-1]
 return g
