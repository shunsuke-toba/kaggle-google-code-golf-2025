def p(g):
 H,W=len(g),len(g[0]);r1=c1=z=0
 for R in range(1,H-1):
  for C in range(1,W-1):
   for s in range(2,min(H-R,W-C)-1):
    R2,C2=R+s,C+s
    if all(g[R-1][c]for c in range(C,C2+1))and all(g[R2+1][c]for c in range(C,C2+1))and all(g[r][C-1]for r in range(R,R2+1))and all(g[r][C2+1]for r in range(R,R2+1)):r1,c1,z=R,C,s
 m=0;r2=c2=0
 for R in range(H-z):
  for C in range(W-z):
   if(R-z-1<=r1<=R+z+1)and(C-z-1<=c1<=C+z+1):continue
   c=sum(g[r][c]>0for r in range(R,R+z+1)for c in range(C,C+z+1))
   if c>m:m=c;r2,c2=R,C
 for r in range(z+1):
  for c in range(z+1):g[r1+r][c1+c]=g[r2+r][c2+c];g[r2+r][c2+c]=0
 for r in range(r1,r1+z+1):
  for c in range(c1,c1+z+1):
   if g[r][c]==0:continue
   u,d,l,ri=r-r1,r1+z-r,c-c1,c1+z-c
   if u<d and u<l and u<ri:g[r][c]=g[r1-1][c]
   if d<u and d<l and d<ri:g[r][c]=g[r1+z+1][c]
   if l<u and l<d and l<ri:g[r][c]=g[r][c1-1]
   if ri<u and ri<d and ri<l:g[r][c]=g[r][c1+z+1]
 return[[g[r][c]for c in range(c1-1,c1+z+2)]for r in range(r1-1,r1+z+2)]