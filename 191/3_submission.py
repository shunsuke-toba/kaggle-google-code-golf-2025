def p(g):
 R=range;L=len;H=L(g);W=L(g[0]);f=sum(g,[]);i=f.index(1);j=L(f)-1-f[::-1].index(1);a=i%W+1;b=j%W;c=i//W+1;d=j//W;m=[[z//4 for z in g[c+Y][a:b]]for Y in R(d-c)];*r,=map(list,g)
 for _ in R(4):
  for q in(m,[s[::-1]for s in m]):
   h=L(q);w=L(q[0])
   for y in R(H-h+1):
    for x in R(W-w+1):
     if all(g[y+v][x+u]==4*q[v][u]for v in R(h)for u in R(w)):
      for V in R(y-1,y+h+1):
       for U in R(x-1,x+w+1):
        if 0<=V<H and 0<=U<W and g[V][U]-4:r[V][U]=1
  m=[*zip(*m)][::-1]
 return r
