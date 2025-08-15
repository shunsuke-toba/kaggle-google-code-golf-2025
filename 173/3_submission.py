def p(g):
 w=len(g[0]);W=w+2;g=[[0]*W]+[[0,*r,0]for r in g]+[[0]*W];h=len(g);m=w*(h-2);S=(A:=((1,0),(-1,0),(0,1),(0,-1)),((1,1),(1,-1),(-1,1),(-1,-1)),A[:2],A[2:]);T=[]
 for i in(R:=range(m)):
  r=i//w+1;c=i%w+1
  if v:=g[r][c]:
   for d in S:
    a=0
    for x,y in d:
     t=g[r+x][c+y]
     if t in(0,v)or a^t and a:break
     a=t
    else:T+=[(d,a,v)]
 z=1
 while z:
  z=0
  for d,a,b in T:
   for i in R:
    r=i//w+1;c=i%w+1;t=g[r][c]
    if t==b:
     for x,y in d:
      if g[r+x][c+y]<1:g[r+x][c+y]=a;z=1
    elif t<1 and all(g[r+x][c+y]==a for x,y in d):g[r][c]=b;z=1
 return[r[1:-1]for r in g[1:-1]]
