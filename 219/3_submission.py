def p(g,R=range):
 i=a=0
 while~-any(g[i]):i+=1
 f=i
 while any(g[i]):a+=1;i+=1
 while i<14:
  i+=1
  if~-any(g[i]):continue
  s=i;n=0
  while any(g[i]):n+=1;i+=1
  M=0
  for t in R(3):
   for S in R(s-a+n,s+1):
    m=1
    if S>g[1][3]==a*4>g[7][7]>g[1][4]:g[12][4]=g[12][6]=g[12][8]=1;m=0
    for j in R(a*10):
     if g[S+j//10][j%10]>1>g[f+j//10][j%10-t]<=j%10-t:m=0
    if m:
     for j in R(a*10):k=j%10;j//=10;g[S+j][k]|=g[f+j][k-t]>1>g[S+j][k]<=k-t;M=1
     break
   if M:break
 return g
