def p(g):
 R=range;r=lambda z:list(map(list,zip(*z[::-1])))
 for k in R(4):
  x,y=zip(*[(i,j)for i,s in enumerate(g)for j,v in enumerate(s)if v])
  a,b=min(x),max(x);c,d=min(y),max(y)
  if 0 in g[a][c+2:d-1]:break
  g=r(g)
 h=[s[:]for s in g];w=d-c-1
 for e in h[a+1:b]:e[c+1:d]=[4]*w
 for e in h[:b]:e[c+2:d-1]=[4]*(w-2)
 for j in R(a):
  i=a-1-j;L=c+1-j;E=d-1+j
  if L>=0:h[i][L]=4
  if E<len(g):h[i][E]=4
 for k in R(-k%4):h=r(h)
 return h
