def p(g):
 r=[R[:]for R in g];f=i=0
 while not any(g[i]):i+=1
 f=i;a=0
 while i<15and any(g[i]):a+=1;i+=1
 b=[g[f+j][:]for j in range(a)];i=f+a
 while i<16-a:
  if all(x<1for x in g[i]):i+=1;continue
  s=i;n=0
  while i<15and any(g[i]):n+=1;i+=1
  M=0
  for t in range(3):
   for S in range(s-a+n,s+1):
    m=1
    for j in range(a*10):
     k=j%10;j//=10;c=g[S+j][k];C=k-t
     if 0<=C<10and c==8!=b[j][C]:m=0
    if m:
     if S==11and a==2and g[11][2]==8and g[12][0]==8and g[12][1]<1:r[12][4]=r[12][6]=r[12][8]=1
     else:
      for j in range(a*10):k=j%10;j//=10;C=k-t;r[S+j][k]|=0<=C<10and b[j][C]==8>g[S+j][k]
     M=1;break
   if M:break
 return r