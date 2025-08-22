def p(g):
 v,A,B=set(),{},{};r=[*map(list,g)]
 for k in range(100):
  y,x=divmod(k,10)
  if(y,x)in v:continue
  c=g[y][x];q=[(y,x)];S={q[0]};f=c<1
  while q:
   y,x=q.pop()
   for Y,X in(y+1,x),(y-1,x),(y,x+1),(y,x-1):
    if 0<=Y<10 and 0<=X<10:
     if g[Y][X]==c:
      if(Y,X)not in S:S.add((Y,X));q.append((Y,X))
     elif f and g[Y][X]-5:f=0
    elif f:f=0
  v|=S;y,x=map(min,zip(*S));s=frozenset((i-y,j-x)for i,j in S)
  if f:A[s]=y,x
  elif c-5:B[c]=c in B and 1 or(s,S,y,x)
 for c,v in B.items():
  if v!=1:
   s,S,y,x=v
   if s in A:
    Y,X=A.pop(s)
    for i,j in S:r[i][j]=0;r[i-y+Y][j-x+X]=c
 return r
