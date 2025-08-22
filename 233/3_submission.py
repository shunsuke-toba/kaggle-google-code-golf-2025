def p(g):
 R=range;T=0,1,2;t=[]
 for y in R(len(g)-2):
  for x in R(len(g[0])-2):
   if len(s:={*sum(b:=[r[x:x+3]for r in g[y:y+3]],[])})<3 and s>{2}>s&{0}:
    t+=b,
    for i in T:g[y+i][x:x+3]=0,0,0
 f=lambda g:[*map(list,zip(*filter(any,zip(*filter(any,g)))))]
 g=f(g)
 t.sort(key=lambda b:-str(b).count('2'))
 for b in t:
  for _ in[0]*4:
   for y in R(len(g)-2):
    for x in R(len(g[0])-2):
     if all((b[i][j]==2)==(g[y+i][x+j]<1)for i in T for j in T):
      for i in T:g[y+i][x:x+3]=b[i]
      break
    else:continue
    break
   else:b=[*zip(*b[::-1])];continue
   break
 return f(g)
