def p(g):
 H=len(g);W=len(g[0]);S={c for r in g for c in r if c};N=((1,0),(-1,0),(0,1),(0,-1))
 for B in S:
  if sum(r.count(B)for r in g)<2:continue
  for A in S-{B}:
   v=[[0]*W for _ in g];found=False
   for y in range(H):
    for x in range(W):
     if v[y][x] or g[y][x]not in(A,B):continue
     q=[(y,x)];v[y][x]=1;ca=cb=0;C=[]
     while q:
      Y,X=q.pop();C.append((Y,X))
      if g[Y][X]==A:ca+=1
      else:cb+=1
      for dy,dx in N:
       ny,nx=Y+dy,X+dx
       if 0<=ny<H and 0<=nx<W and not v[ny][nx] and g[ny][nx]in(A,B):v[ny][nx]=1;q.append((ny,nx))
     if cb==1 and ca>1:
      ay,ax=[p for p in C if g[p[0]][p[1]]==B][0]
      off=[(y-ay,x-ax)for y,x in C if g[y][x]==A]
      found=True
      break
    if found:break
   if found:break
  if found:break
 if not found:return g
 r=[row[:]for row in g];v=[[0]*W for _ in g]
 for y in range(H):
  for x in range(W):
   if g[y][x]==B and not v[y][x]:
    q=[(y,x)];v[y][x]=1;C=[];mnx=mny=10**9;mx=my=-10**9
    while q:
     Y,X=q.pop();C.append((Y,X))
     mny=min(mny,Y);my=max(my,Y);mnx=min(mnx,X);mx=max(mx,X)
     for dy,dx in N:
      ny,nx=Y+dy,X+dx
      if 0<=ny<H and 0<=nx<W and not v[ny][nx] and g[ny][nx]==B:v[ny][nx]=1;q.append((ny,nx))
    n=max(my-mny+1,mx-mnx+1);col=A
    for Y,X in C:
     for dy,dx in N:
      ny,nx=Y+dy,X+dx
      if 0<=ny<H and 0<=nx<W:
       c=g[ny][nx]
       if c not in(0,B):col=c;break
     else:continue
     break
    for dy,dx in off:
     sy=mny+dy*n; sx=mnx+dx*n
     for yy in range(sy,sy+n):
      for xx in range(sx,sx+n):
       if 0<=yy<H and 0<=xx<W:r[yy][xx]=col
 return r
