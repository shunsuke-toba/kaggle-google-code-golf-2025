def p(g):
 R=range;L=len;H=L(g);W=L(g[0]);f=sum(g,[]);i=f.index(1);k=f[::-1].index(1);a=i%W+1;b=~k%W;c=i//W+1;d=H-1-k//W;m=[[z//4 for z in g[y][a:b]]for y in R(c,d)];*r,=map(list,g)
 for _ in R(4):
  for q in m,m[::-1]:
   h=L(q);w=L(q[0])
   for y in R(H-h+1):
    for x in R(W-w+1):
     if all(g[y+v][x+u]==4*q[v][u]for v in R(h)for u in R(w)):
      for V in R(y-1,y+h+1):
       for U in R(x-1,x+w+1):
        if-1<V<H and-1<U<W and g[V][U]-4:r[V][U]=1
  m=[*zip(*m[::-1])]
 return r
