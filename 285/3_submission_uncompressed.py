def p(g):
 o=[r[:]for r in g];n=len(g)
 for y in range(n):
  for x in range(n):
   if c:=o[y][x]:
    o[y][x]=0;q=[(y,x)]
    for i,j in q:
     for b in-1,0,1:
      for a in-1,0,1:
       if v:=o[(i+a)%n][(j+b)%n]:
        if v==c:o[(i+a)%n][(j+b)%n]=0;q+=((i+a)%n,(j+b)%n),
    for i,j in q:
     for b in-1,0,1:
      for a in-1,0,1:
       if v:=o[(i+a)%n][(j+b)%n]:
        if a*b==0:y,x=i,j
    for i,j in q:
     for b in-1,0,1:
      for a in-1,0,1:
       if v:=o[(y+a)%n][(x+b)%n]:g[(i,2*y+a-i)[a&1]][(j,2*x+b-j)[b&1]]=v
    o[y][x]=c
 return g