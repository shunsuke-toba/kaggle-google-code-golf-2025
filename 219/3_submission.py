def p(g):
 def f(t,o,m,g):
  W=len(g[0]);H=len(g);p=[];z=1;h=c=0
  for r in range(H):
   if sum(g[r])<1:z=1
   elif z:p+=r,;z=0;c=1
   else:c+=1
   h=max(h,c)
  R=range(h)
  F=p[0];b=[*map(list,g[F:F+h])]
  for s in p[1:]:
   r=s+o
   if r<0 or r+h>H:return
   for i in range(W+~t,-1,-1):
    if i+t+1<W and sum(sum(g[r+j][i+t:i+t+2])for j in R):continue
    T=range(t);a=sum(g[r+j][i+x]<<(x*h+j)for j in R for x in T)
    for j in range(W-t):
     if m*(j-i):continue
     if (c:=j+t)+2<W and a==sum(b[y][j+x]<<(x*h+y)for y in R for x in T) and all(r[c]==r[c+2]for r in b):
      for d in range(W-i-t):
       for y in R:g[r+y][i+t+d]=b[y][c+d%2]//8
      break
    else:continue
    break
   else:return
  return g
 u=[*map(list,g)]
 for t in 3,2:
  for m in 1,0:
   for o in 0,-1:
    if v:=f(t,o,m,[*map(list,u)]):return v
