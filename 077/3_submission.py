def p(g):
 e=enumerate
 S={(i,j)for i,r in e(g)for j,v in e(r)if v==2}
 while S:
  T={S.pop()}
  while U:=S&{(y+i//5-2,x+i%5-2)for i in range(25)for y,x in T}:T|=U;S-=U
  y,x=zip(*T);a,b=min(y),max(y)+1;c,d=min(x),max(x)+1
  for r in g[a:b]:r[c:d]=[4>>(v==2)for v in r[c:d]]
 return g
