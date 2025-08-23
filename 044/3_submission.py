def p(g):
 r=[*map(list,g)]
 a={};b={}
 for k in range(100):
  y,x=divmod(k,10);c=g[y][x]
  if c-5:
   q=[(y,x)];g[y][x]=5;f=c<1
   for y,x in q:
    for Y,X in(y+1,x),(y-1,x),(y,x+1),(y,x-1):
     if 0<=Y<10 and 0<=X<10:
      d=g[Y][X]
      if d==c:g[Y][X]=5;q.append((Y,X))
      elif f and d-5:f=0
     elif f:f=0
   Y,X=map(min,zip(*q));s=frozenset((i-Y,j-X)for i,j in q)
   if f:a[s]=Y,X
   elif c:b[c]=c in b or not q[1:] and 1 or(s,q,Y,X)
 for c,v in b.items():
  if v!=1 and v[0] in a:
   s,q,y,x=v
   Y,X=a[s]
   for i,j in q:r[i][j]=0;r[i-y+Y][j-x+X]=c
 return r
