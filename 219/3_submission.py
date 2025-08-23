def p(g):
 def f(t,o,m,g):
  w=len(g[0]);H=len(g);p=[];z=1;h=c=0
  for r in range(H):
   if sum(g[r])<1:z=1
   elif z:p+=r,;z=0;c=1
   else:c+=1
   h=max(h,c)
  R=range(h)
  b=[*map(list,g[p[0]:p[0]+h])]
  for s in p[1:]:
   if 0>(r:=s+o) or r+h>H:return
   for i in range(w+~t,-1,-1):
    if i+t+1<w and sum(sum(g[r+j][i+t:i+t+2])for j in R):continue
    T=range(t);a=sum(g[r+j][i+x]<<(x*h+j)for j in R for x in T)
    for j in range(w-t):
     if m*(j-i):continue
     if (c:=j+t)+2<w and a==sum(b[y][j+x]<<(x*h+y)for y in R for x in T) and all(r[c]==r[c+2]for r in b):
      for d in range(w-i-t):
       for y in R:g[r+y][i+t+d]=b[y][c+d%2]//8
      break
    else:continue
    break
   else:return
  return g
 for t in 3,2:
  for m in 1,0:
   for o in 0,-1:
    if f(t,o,m,a:=[*map(list,g)]):return a
