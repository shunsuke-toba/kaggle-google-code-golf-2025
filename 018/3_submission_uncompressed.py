def p(g):
 w=len(g[0]);S=[]
 for y in range(len(g)*w):
  x=y%w;y//=w;a=0
  for Y in range(y+1,len(g)+1):
   for X in range(x+1,w+1):
    if len({*sum(m:=[q[x:X]for q in g[y:Y]],[0])})*all(map(sum,m+[*zip(*m)]))>4:a,b,r=Y,X,m
  if a:S+=r,
  for t in g[y:a]:t[x:b]=[0]*(b-x)
 for r in S:
  for z in range(8):
   for y in range(len(g)-(a:=len(r))+1):
    for x in range(w-(b:=len(r[0]))+1):
     if all((str(r).count(str(c:=r[k//b][k%b]))<2)*c==g[y+k//b][x+k%b]for k in range(a*b)):
      for i in range(a):g[y+i][x:x+b]=r[i]
   r=[*zip(*r[::-1])];z^3or r.reverse()
 return g