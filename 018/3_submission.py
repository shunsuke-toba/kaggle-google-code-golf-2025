def p(g):
 R=range;L=len;h,w=L(g),L(g[0]);s=[]
 for y in R(h):
  for x in R(w):
   a=b=0
   for Y in R(y+1,h+1):
    for X in R(x+1,w+1):
     if all(map(any,(m:=[q[x:X]for q in g[y:Y]])+[*zip(*m)]))and L({0,*sum(m,[])})>4:a,b,r=Y,X,m
   if a:s+=r,
   for t in g[y:a]:t[x:b]=[0]*(b-x)
 for r in s:
  u=sum(r,[])
  for z in R(8):
   for y in R(h-(a:=L(r))+1):
    for x in R(w-(b:=L(r[0]))+1):
     if all(r[i][j]*(u.count(r[i][j])<2)==g[y+i][x+j]for i in R(a)for j in R(b)):
      for i in R(a):g[y+i][x:x+b]=r[i]
   r=[*zip(*r[::-1])];z-3or r.reverse()
 return g
