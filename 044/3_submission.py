def p(g):
 h=len(g);w=len(g[0]);v,A,B=set(),[],{}
 for k in range(h*w):
  y,x=divmod(k,w)
  if(y,x)in v:continue
  c=g[y][x];q=[(y,x)];S={*q};f=1
  while q:
   y,x=q.pop()
   for Y,X in(y+1,x),(y-1,x),(y,x+1),(y,x-1):
    if 0<=Y<h and 0<=X<w:
     if g[Y][X]==c:
      if(Y,X)not in S:S.add((Y,X));q.append((Y,X))
     elif c<1 and g[Y][X]-5:f=0
    elif c<1:f=0
  v|=S;y,x=map(min,zip(*S));s={(i-y,j-x)for i,j in S}
  if c<1:f and A.append((s,y,x))
  elif c-5:B[c]=B.get(c,[])+[(s,S,y,x)]
 r=[*map(list,g)]
 for c in B:
  b=B[c]
  if b[1:]:continue
  s,b,y,x=b[0]
  for t,Y,X in A:
   if s==t:
    for i,j in b:r[i][j]=0;r[i-y+Y][j-x+X]=c
    break
 return r
