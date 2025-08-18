def p(g,R=range):
 H,W,m,z=len(g),len(g[0]),None,0
 for k in R(H*W*H*W):
  r1,k=divmod(k,W*H*W);c1,k=divmod(k,H*W);r2,c2=divmod(k,W)
  if r1+2<=r2<H and c1+2<=c2<W:
   a=all(g[r1][c]==2and g[r2][c]==2for c in R(c1,c2+1))
   if a and(r2-r1)*(c2-c1)>z:m,z=(r1,c1,r2,c2),(r2-r1)*(c2-c1)
 def h(p,t):return sum(1<<k for k in R(9)if p[k//3][k%3]==t)
 def rt(p):return[[p[2-c][r]for c in R(3)]for r in R(3)]
 r1,c1,r2,c2=m;p=[]
 for k in R((H-2)*(W-2)):
  r,c=divmod(k,W-2)
  if r1-2<=r<=r2-2and c1-2<=c<=c2-2:continue
  t=[[g[r+dr][c+dc]for dc in R(3)]for dr in R(3)];z=n=w=0
  for j in R(9):
   v=t[j//3][j%3]
   if v<1:z=1
   if v!=2:n=v
   else:w+=1
  if not z:
   for o in R(4):p+=((w,-o,h(t,2),n)),;t=rt(t)
 p.sort(reverse=True)
 L=R(r1,r2-1);M=R(c1,c2-1)
 for _,_,q,n in p:
  for k in R(len(L)*len(M)):
   r,c=L[k//len(M)],M[k%len(M)]
   t=h([[g[r+dr][c+dc]for dc in R(3)]for dr in R(3)],0)
   if q==t:
    for j in R(9):
     dr,dc=divmod(j,3)
     if g[r+dr][c+dc]==2:g[r+dr][c+dc]=n
     elif g[r+dr][c+dc]<1:g[r+dr][c+dc]=2
 return[[g[r][c]for c in R(c1,c2+1)]for r in R(r1,r2+1)]
