def p(g):
 import random
 def s(g):
  z=[i for i in range(len(g[0]))if all(g[j][i]==0for j in range(3))]+[len(g[0])]
  l=0
  for r in z:
   n=5
   for _ in[1]*2:
    for i in range(3):
     for j in range(l,r):
      if g[i][j]%5:n=g[i][j]
      elif g[i][j]==5:g[i][j]=n
   l=r+1
  p=0;S=0;R=[[0]*(len(g[0])-len(z)+1)for _ in range(3)]
  for j in range(len(g[0])):
   if j in z:S=random.randint(0,2);continue
   for i in range(3):R[i][p]=g[(i+S)%3][j]
   p+=1
  y=1
  for j in range(p):
   if R[0][j]and R[1][j]==0and R[2][j]:return
   y1,y2=2,0
   for i in range(3):
    if R[i][j]:y1,y2=min(y1,i),max(y2,i)
   if y1==y:y=y2
   elif y2==y:y=y1
   else:return
  return R
 for _ in[1]*999:
  G=[[g[i][j]for j in range(len(g[0]))]for i in range(3)];r=s(G)
  if r:return r