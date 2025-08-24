def p(g,A=range):
 def f(t,o,m,g):
  w=10;p=[];z=1;h=c=0
  for r in A(15):
   if sum(g[r])<1:z=1
   elif z:p+=r,;z=0;c=1
   else:c+=1
   h=max(h,c)
  R=A(h);b=g[p[0]:p[0]+h]
  for s in p[1:]:
   if 0>(r:=s+o)or r+h>15:return
   for i in A(w+~t,-1,-1):
    if i+t+1<w and sum(sum(g[r+j][i+t:i+t+2])for j in R):continue
    for j in A(w-t):
     if(j-i)*m:continue
     if(c:=j+t)+2<w and all(g[r+y][i:i+t]==b[y][j:j+t]for y in R)and all(r[c]==r[c+2]for r in b):
      for d in A(w-i-t):
       for y in R:g[r+y][i+t+d]=b[y][c+d%2]>0
      break
    else:continue
    break
   else:return
  return g
 for t in 3,2:
  for m in 1,0:
   for o in 0,-1:
    if f(t,o,m,a:=eval(str(g))):return a