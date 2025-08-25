def p(g):
 e=enumerate
 S={(i,j)for i,r in e(g)for j,v in e(r)if v==2}
 while S:
  T={S.pop()}
  while U:=S&{(y+i//5-2,x+i%5-2)for i in range(25)for y,x in T}:T|=U;S-=U
  y,x=zip(*T)
  for r in g[min(y):max(y)+1]:r[min(x):max(x)+1]=[4>>(v==2)for v in r[min(x):max(x)+1]]
 return g
