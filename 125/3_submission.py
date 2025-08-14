def p(g):
 m,n=len(g),len(g[0]);r=[*map(list,g)];V=set()
 for y in range(m):
  for x in range(n):
   if g[y][x]==6 and(y,x)not in V:
    a=b=y;c=d=x;s=[(y,x)]
    while s:
     i,j=s.pop()
     if(i,j)in V:continue
     V.add((i,j));a=min(a,i);b=max(b,i);c=min(c,j);d=max(d,j)
     for u,v in(1,0),(-1,0),(0,1),(0,-1):
      Y,X=i+u,j+v
      if 0<=Y<m and 0<=X<n and g[Y][X]==6:s.append((Y,X))
    for i in range(a+1,b):
     for j in range(c+1,d):
      if r[i][j]==8:r[i][j]=4
 for y,x in V:
  for i in range(max(0,y-1),min(m,y+2)):
   for j in range(max(0,x-1),min(n,x+2)):
    if r[i][j]==8:r[i][j]=3
 return r
