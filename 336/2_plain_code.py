def p(g):
 n,m=len(g),len(g[0])
 t=n;b=-1;l=m;r=-1
 for i,row in enumerate(g):
  for j,v in enumerate(row):
   if v==5:t=min(t,i);b=max(b,i);l=min(l,j);r=max(r,j)
 for i in range(t+1,b):
  for j in range(l+1,r):g[i][j]=8
 hr=hc=None
 for j in range(l,r+1):
  if g[t][j]!=5:hr,hd=t,j;dr,dc=-1,0;break
 if hr is None:
  for j in range(l,r+1):
   if g[b][j]!=5:hr,hd=b,j;dr,dc=1,0;break
 if hr is None:
  for i in range(t,b+1):
   if g[i][l]!=5:hr,hd=i,l;dr,dc=0,-1;break
 if hr is None:
  for i in range(t,b+1):
   if g[i][r]!=5:hr,hd=i,r;dr,dc=0,1;break
 i,j=hr,hd
 while 0<=i<n and 0<=j<m:g[i][j]=8;i+=dr;j+=dc
 return g