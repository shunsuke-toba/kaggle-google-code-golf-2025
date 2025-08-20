def p(g):
 h=len(g);w=len(g[0]);u=[[0]*w for _ in g];f=lambda y,x:(g[y][x]==2)-(g[y][x] in(0,8))*10-100*u[y][x];m=5
 while 1:
  B=S=I=J=0
  for s in 7,5:
   if m>s:continue
   r=s//2
   for i in range(h):
    for j in range(w):
     b=0
     for d in range(-r,r+1):
      a=i+d
      if-1<a<h:b+=f(a,j)
      c=j+d
      if d and-1<c<w:b+=f(i,c)
     if (b,-s)>(B,-S):B,S,I,J=b,s,i,j
  if B<1:return g
  r=S//2;m=S
  for d in range(-r,r+1):
   a=I+d;c=J+d
   if-1<a<h:u[a][J]=1;g[a][J]+=3*(g[a][J]==5)
   if d and-1<c<w:u[I][c]=1;g[I][c]+=3*(g[I][c]==5)
