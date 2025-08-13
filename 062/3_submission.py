def p(g):
 h,w=len(g),len(g[0])
 v=[[0]*w for _ in range(h)]
 C=[]
 def d(i,j,c,a):
  if i<0 or i>=h or j<0 or j>=w or v[i][j] or g[i][j]!=c:return
  v[i][j]=1;a.append((i,j))
  for di,dj in[(0,1),(0,-1),(1,0),(-1,0)]:d(i+di,j+dj,c,a)
 for i in range(h):
  for j in range(w):
   if not v[i][j] and g[i][j]:a=[];d(i,j,g[i][j],a);C.append((g[i][j],a))
 r=[[3]*w for _ in range(h)]
 if not C:return r
 c,L=max(C,key=lambda x:len(x[1]))
 for i in range(h):
  for j in range(w):
   if g[i][j]:r[i][j]=g[i][j]
 ys=[p[0]for p in L];xs=[p[1]for p in L]
 my,My=min(ys),max(ys);mx,Mx=min(xs),max(xs)
 R=[]
 T=[]
 for y,x in L:
  ny=my-(y-my)-1
  if 0<=ny<h:T.append((ny,x))
 if T:R.append(T);T=[]
 for y,x in L:
  ny=My+(My-y)+1
  if 0<=ny<h:T.append((ny,x))
 if T:R.append(T);T=[]
 for y,x in L:
  nx=mx-(x-mx)-1
  if 0<=nx<w:T.append((y,nx))
 if T:R.append(T);T=[]
 for y,x in L:
  nx=Mx+(Mx-x)+1
  if 0<=nx<w:T.append((y,nx))
 if T:R.append(T)
 for T in R:
  if any(g[y][x]for y,x in T if 0<=y<h and 0<=x<w):
   for y,x in T:
    if 0<=y<h and 0<=x<w:r[y][x]=c
 return r
