def p(j,A=range):
 c,E=len(j),len(j[0])
 def f(x,y):
  j[x][y]=0
  for a,b in(1,0),(-1,0),(0,1),(0,-1):c>x+a>-1<y+b<E and j[x+a][y+b]and f(x+a,y+b)
 k=sum(j[i][d]and(f(i,d)or 1)for i in A(c)for d in A(E))
 return[[8*(i==y)for y in A(k)]for i in A(k)]