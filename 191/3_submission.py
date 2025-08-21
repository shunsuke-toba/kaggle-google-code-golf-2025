def p(g):
 R=range;L=len;S=L(g);f=sum(g,[]);i=f.index(1);k=f[::-1].index(1);a=i%S+1;b=~k%S;c=i//S+1;d=S-1-k//S
 m=[[x>1 for x in r[a:b]]for r in g[c:d]];r=[*map(list,g)]
 for _ in R(4):
  for q in m,m[::-1]:
   h=L(q);w=L(q[0])
   for y in R(S-h+1):
    for x in R(S-w+1):
     if all(g[y+v][x+u]==4*q[v][u]for v in R(h)for u in R(w)):
      for V in R(y-1,y+h+1):
       for U in R(x-1,x+w+1):
        if S>V>=0<=U<S and g[V][U]-4:r[V][U]=1
  m=[*zip(*m[::-1])]
 return r
