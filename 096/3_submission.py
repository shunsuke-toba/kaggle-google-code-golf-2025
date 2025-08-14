def p(g):
 import re
 X=range
 r,c=len(g),len(g[0])
 C=[0]*10
 for i in X(r):
  for j in X(c):C[g[i][j]]+=1
 b=C.index(max(C))
 I=[]
 for x in X(10):
  if x==b:continue
  s=None
  for w in X(2,9):
   for d in X(1,15):
    for _ in X(4):
     if any(re.search(str(x)*w+f"[^{x}]"*d+str(x),"".join(map(str,R)))for R in g):s=(x,w,d)
     g=[list(R)for R in zip(*g[::-1])]
  if not s and C[x]==1:s=(x,1,-1)
  if not s and C[x]:s=(x,3,-3)
  if s:I.append(s)
 I.sort(key=lambda y:y[1]*2+y[2])
 z=I[-1][1]*2+I[-1][2]
 R=[[b]*z for _ in X(z)]
 i=0
 while I:
  J=I.pop()
  for _ in X(4):
   for k in X(J[1]):R[i][i+k]=R[i+k][i]=J[0]
   R=[list(row)for row in zip(*R[::-1])]
  i+=1
 return R