def p(g):
 L=len;A=all;R=range;S=[]
 h=L(g);w=L(g[0])
 for y in R(h):
  for x in R(w):
   a=b=0
   for Y in R(y+1,h+1):
    for X in R(x+1,w+1):
     if (m:=[r[x:X]for r in g[y:Y]])and A(map(any,m+[*zip(*m)]))and L({0,*sum(m,[])})>4:a,b,M=Y,X,m
   if a:S+=M,
   for r in g[y:a]:r[x:b]=[0]*(b-x)
 for r in S:
  u=sum(r,[])
  for z in R(8):
   a=L(r);b=L(r[0])
   for y in R(h-a+1):
    for x in R(w-b+1):
     if A(r[i][j]*(u.count(r[i][j])<2)==g[y+i][x+j]for i in R(a)for j in R(b)):
      for i in R(a):g[y+i][x:x+b]=r[i]
   r=[*zip(*r[::-1])]
   if z&3>2:r=r[::-1]
 return g
