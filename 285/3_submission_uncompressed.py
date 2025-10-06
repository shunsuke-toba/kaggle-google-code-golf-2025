def p(g):
 o=[r[:]for r in g];n=len(g)
 for y in range(n):
  for x in range(n):
   if v:=o[y][x]:
    c=v;o[y][x]=0;q=[(y,x)]
    for y,x in q:
     for a in -1,0,1:
      for b in -1,0,1:
       if v:=o[(y+a)%n][(x+b)%n]:
        if v==c:o[(y+a)%n][(x+b)%n]=0;q+=((y+a)%n,(x+b)%n),
    for y,x in q:
     for a in -1,0,1:
      for b in -1,0,1:
       if v:=o[(y+a)%n][(x+b)%n]:
        if a*b==0:u,w=y,x
    for y,x in q:
     for a in -1,0,1:
      for b in -1,0,1:
       if v:=o[(u+a)%n][(w+b)%n]:g[(y,2*u+a-y)[a%2]][(x,2*w+b-x)[b%2]]=v
    o[u][w]=c
 return g
