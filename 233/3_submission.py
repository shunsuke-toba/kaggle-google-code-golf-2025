def p(g):
 R=range;T=R(3);t=[]
 for y in R(len(g)-2):
  for x in R(len(g[0])-2):
   if len(s:={*sum(b:=[r[x:x+3]for r in g[y:y+3]],[])})<3 and s>{2}>s&{0}:
    t+=b,
    for i in T:g[y+i][x:x+3]=0,0,0
 g=[*map(list,zip(*filter(any,zip(*filter(any,g)))))]
 t.sort(key=lambda b:-str(b).count('2'))
 for b in t:
  for _ in R(4):
   try:
    y,x=next((y,x)for y in R(len(g)-2)for x in R(len(g[0])-2)if all((b[i][j]==2)==(g[y+i][x+j]<1)for i in T for j in T))
   except:
    b=[*zip(*b[::-1])]
   else:
    for i in T:g[y+i][x:x+3]=b[i]
    break
 return g
