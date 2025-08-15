def p(g):
 o=[r[:]for r in g];h=len(g);w=len(g[0]);E=((1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1));F=E[:4];v=[[0]*w for _ in g]
 for i in range(h):
  for j in range(w):
   if o[i][j]and not v[i][j]:
    q=[(i,j)];v[i][j]=1
    for y,x in q:
     for a,b in E:
      Y=y+a;X=x+b
      if 0<=Y<h and 0<=X<w and o[Y][X]and not v[Y][X]:v[Y][X]=1;q+=((Y,X),)
    A=[o[y][x]for y,x in q];m=max(A,key=A.count)
    B=next((y,x)for y,x in q if o[y][x]==m and any(0<=y+a<h and 0<=x+b<w and 0<o[y+a][x+b]!=m for a,b in F))
    y,x=B;O=[(r-y,c-x)for r,c in q if o[r][c]==m]
    for a,b in E:
     ny=y+a;nx=x+b;c=0<=ny<h and 0<=nx<w and o[ny][nx]
     if 0<c!=m:
      for oy,ox in O:
       ty=ny-oy if a else ny+oy
       tx=nx-ox if b else nx+ox
       if 0<=ty<h and 0<=tx<w:g[ty][tx]=c
 return g
