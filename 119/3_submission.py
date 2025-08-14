def p(g):
 m,n=len(g),len(g[0]);R=[*map(list,g)]
 for y in range(m):
  for x in range(n):
   c=R[y][x]
   if c in(0,2,3):continue
   for v,w in((-1,-1),(-1,1),(1,-1),(1,1)):
    Y,X=y+v,x+w
    if 0<=Y<m and 0<=X<n and R[Y][X]==c:
     i,j=y,x;dy,dx=v,w
     while 1:
      Y,X=i+dy,j+dx
      if not(0<=Y<m and 0<=X<n):break
      t=R[Y][X]
      if t==2:
       V=(Y>0 and R[Y-1][X]==2)+(Y<m-1 and R[Y+1][X]==2)
       H=(X>0 and R[Y][X-1]==2)+(X<n-1 and R[Y][X+1]==2)
       if V>H:dx=-dx
       elif H>V:dy=-dy
       elif V:dx=-dx
       else:break
      elif t in(0,c,3):R[Y][X]=t or 3;i,j=Y,X
      else:break
 return R
