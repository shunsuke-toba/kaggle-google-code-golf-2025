def p(g):
 H=len(g);W=len(g[0])
 from collections import deque as D
 V=[[0]*W for _ in g];B=None
 for i in range(H):
  for j in range(W):
   if g[i][j]>0 and not V[i][j]:
    q=D([(i,j)]);V[i][j]=1;c=[];a=b=0
    while q:
     x,y=q.popleft();c+=x,y;v=g[x][y];a|=v==1;b|=v==2
     for X,Y in((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
      if 0<=X<H and 0<=Y<W and g[X][Y] and not V[X][Y]:V[X][Y]=1;q.append((X,Y))
    if a and b and B is None:B=c
 if not B:return g
 xs=B[0::2];ys=B[1::2]
 x0,x1=min(xs),max(xs);y0,y1=min(ys),max(ys)
 P=[r[y0:y1+1] for r in g[x0:x1+1]]
 B1=[(i,j) for i,r in enumerate(P) for j,v in enumerate(r) if v==1]
 B2=[(i,j) for i,r in enumerate(P) for j,v in enumerate(r) if v==2]
 R={(i,j) for i in range(H) for j in range(W) if g[i][j]==2 and (i,j) not in {(B[i],B[i+1]) for i in range(0,len(B),2)}}
 xs2=[r for r,_ in B2];ys2=[c for _,c in B2]
 for k in range(max(H,W),0,-1):
  for r0 in range(-min(xs2)*k,H-(max(xs2)+1)*k+1):
   for c0 in range(-min(ys2)*k,W-(max(ys2)+1)*k+1):
    U=[];ok=1
    for r,c in B2:
     for Rr in range(r0+r*k,r0+(r+1)*k):
      for Cc in range(c0+c*k,c0+(c+1)*k):
       if not(0<=Rr<H and 0<=Cc<W and g[Rr][Cc]==2 and (Rr,Cc) in R):ok=0;break
       U.append((Rr,Cc))
      if not ok:break
     if not ok:break
    if not ok:continue
    for r,c in B1:
     for Rr in range(r0+r*k,r0+(r+1)*k):
      for Cc in range(c0+c*k,c0+(c+1)*k):
       if 0<=Rr<H and 0<=Cc<W and g[Rr][Cc]!=0:ok=0;break
      if not ok:break
     if not ok:break
    if not ok:continue
    for r,row in enumerate(P):
     for c,val in enumerate(row):
      for Rr in range(r0+r*k,r0+(r+1)*k):
       for Cc in range(c0+c*k,c0+(c+1)*k):
        if 0<=Rr<H and 0<=Cc<W:g[Rr][Cc]=val
    for cell in U:R.discard(cell)
 return g
