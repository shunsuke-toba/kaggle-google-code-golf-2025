def p(g):
 def s(g,R,C):
  H,W,m,z=len(g),len(g[0]),None,0
  for k in range(H*W*H*W):
   r1,k=divmod(k,W*H*W);c1,k=divmod(k,H*W);r2,c2=divmod(k,W)
   if r1+2<=r2<H and c1+2<=c2<W:
    a=all(g[r1][c]==2and g[r2][c]==2for c in range(c1,c2+1))and all(g[r][c1]==2and g[r][c2]==2for r in range(r1,r2+1))
    if a and(r2-r1+1)*(c2-c1+1)>z:m,z=(r1,c1,r2,c2),(r2-r1+1)*(c2-c1+1)
  def h(p,t):return sum(1<<k for k in range(9)if p[k//3][k%3]==t)
  def rt(p):return[[p[2-c][r]for c in range(3)]for r in range(3)]
  r1,c1,r2,c2=m;p=[]
  for k in range((H-2)*(W-2)):
   r,c=divmod(k,W-2)
   if r1-2<=r<=r2-2and c1-2<=c<=c2-2:continue
   t=[[g[r+dr][c+dc]for dc in range(3)]for dr in range(3)];z=n=0
   for j in range(9):
    v=t[j//3][j%3]
    if v<1:z=1
    if v!=2:n=v
   if not z:
    for _ in[1]*4:p+=((h(t,2),n)),;t=rt(t)
  L=range(r1,r2-1);M=range(c1,c2-1)
  if R:L=L[::-1]
  if C:M=M[::-1]
  for k in range(len(L)*len(M)):
   r,c=L[k//len(M)],M[k%len(M)]
   o=1
   if g[r][c]<1or g[r][c+1]<1or g[r][c+2]<1:
    if r and(g[r-1][c]<1or g[r-1][c+1]<1or g[r-1][c+2]<1):o=0
   if g[r+2][c]<1or g[r+2][c+1]<1or g[r+2][c+2]<1:
    if r+3<H and(g[r+3][c]<1or g[r+3][c+1]<1or g[r+3][c+2]<1):o=0
   if g[r][c]<1or g[r+1][c]<1or g[r+2][c]<1:
    if c and(g[r][c-1]<1or g[r+1][c-1]<1or g[r+2][c-1]<1):o=0
   if g[r][c+2]<1or g[r+1][c+2]<1or g[r+2][c+2]<1:
    if c+3<W and(g[r][c+3]<1or g[r+1][c+3]<1or g[r+2][c+3]<1):o=0
   if o:
    t=h([[g[r+dr][c+dc]for dc in range(3)]for dr in range(3)],0)
    for q,n in p:
     if q==t:
      for j in range(9):
       dr,dc=divmod(j,3)
       if g[r+dr][c+dc]==2:g[r+dr][c+dc]=n
       elif g[r+dr][c+dc]<1:g[r+dr][c+dc]=2
      break
  for k in range((r2-r1+1)*(c2-c1+1)):
   r,c=r1+k//(c2-c1+1),c1+k%(c2-c1+1)
   if g[r][c]<1:return
  return[[g[r][c]for c in range(c1,c2+1)]for r in range(r1,r2+1)]
 L=0,1
 if len(g)!=24:L=1,0
 for k in range(4):
  R,C=k//2,L[k%2]
  if r:=s([r[:]for r in g],R,C):return r