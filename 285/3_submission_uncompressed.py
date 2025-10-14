def p(g):
 o=[r[:]for r in g];n=len(g)
 for y in range(n):
  for x in range(n):
   if c:=o[y][x]:
    o[y][x]=0;q=[(y,x)]
    for y,x in q:
     for b in-1,0,1:
      for a in-1,0,1:
       if v:=o[(y+a)%n][(x+b)%n]:
        if v==c:o[(y+a)%n][(x+b)%n]=0;q+=((y+a)%n,(x+b)%n),
    for y,x in q:
     for b in-1,0,1:
      for a in-1,0,1:
       if v:=o[(y+a)%n][(x+b)%n]:
        if a*b==0:u,w=y,x
    for y,x in q:
     for b in-1,0,1:
      for a in-1,0,1:
       if v:=o[(u+a)%n][(w+b)%n]:g[(y,2*u+a-y)[a&1]][(x,2*w+b-x)[b&1]]=v
    o[u][w]=c
 return g