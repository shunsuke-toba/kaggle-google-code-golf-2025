def p(g):
 h=len(g);w=len(g[0]);R=range;F=filter;p=[]
 for r in R(h):
  for c in R(w):
   q,u,v=[],r,c
   for s in R(r+1,h+1):
    for t in R(c+1,w+1):
     if (x:=[g[i][c:t] for i in R(r,s)])==[*map(list,zip(*F(any,zip(*list(F(any,x))))))]:
      if len({*sum(x,[]),0})>4:q,u,v=x,s,t
   if q:p+=[q]
   for i in R(r,u): g[i][c:v]=[0]*(v-c)
 for r in p:
  for z in R(8):
   H,W=len(r),len(r[0])
   for y in R(h-H+1):
    for x in R(w-W+1):
     if all(r[i][j]*(sum(r,[]).count(r[i][j])==1)==g[y+i][x+j] for i in R(H) for j in R(W)):
      for i in R(H): g[y+i][x:x+W]=r[i]
   r=list(map(list, zip(*r[::-1])))
   if z&3>2:r=r[::-1]
 return g
