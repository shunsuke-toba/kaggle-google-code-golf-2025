def p(g):
 R=range;L=len;h,w=L(g),L(g[0]);S=[]
 for y in R(h):
  for x in R(w):
   a=b=0
   for Y in R(y+1,h+1):
    for X in R(x+1,w+1):
     if (L({0,*sum(m:=[q[x:X]for q in g[y:Y]],[])})>4)&all(map(any,m+[*zip(*m)])):a,b,r=Y,X,m
   if a:S+=r,
   for t in g[y:a]:t[x:b]=[0]*(b-x)
 for r in S:
  u=sum(r,[])
  for z in R(8):
   a,b=L(r),L(r[0])
   for y in R(h-a+1):
    for x in R(w-b+1):
     if all((u.count(c:=r[i][j])<2)*c==g[y+i][x+j]for i in R(a)for j in R(b)):
      for i in R(a):g[y+i][x:x+b]=r[i]
   r=[*zip(*r[::-1])];z^3or r.reverse()
 return g