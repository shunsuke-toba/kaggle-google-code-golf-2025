def p(g):
 h,w=len(g),len(g[0]);V=[[0]*w for _ in[0]*h];B=[]
 for k in range(h*w):
  i,j=k//w,k%w
  if g[i][j]==3 and not V[i][j]:
   r=i;y=j
   while y+1<w and g[i][y+1]==3:y+=1
   while r+1<h and g[r+1][j]==3:r+=1
   for a in range(i,r+1):
    for b in range(j,y+1):V[a][b]=1
   B+=[(i,j,r-i+1)]
 if not B:return g
 n=B[0][2];R=[r[:]for r in g];U=set();D=[]
 for i in range(len(B)):
  if i in U:continue
  b=B[i];d=[b];U.add(i)
  for j in range(i+1,len(B)):
   if j in U:continue
   e=B[j];r=e[0]-b[0];c=e[1]-b[1]
   if r==c==n or r==-c==n:d+=[e];U.add(j)
  if len(d)>1:D+=[d]
 for d in D:
  d.sort();a,b=d[0],d[-1];t=b[1]>a[1]
  for k in range(n*n):
   i,j=k//n,k%n;r,c=a[0]-n+i,b[1]+n+j;x,y=b[0]+n+i,a[1]-n+j
   if t and 0<=r<h and 0<=c<w:R[r][c]=8
   if t and 0<=x<h and 0<=y<w:R[x][y]=8
   r,c=a[0]-n+i,b[1]-n+j;x,y=b[0]+n+i,a[1]+n+j
   if not t and 0<=r<h and 0<=c<w:R[r][c]=8
   if not t and 0<=x<h and 0<=y<w:R[x][y]=8
 return R
