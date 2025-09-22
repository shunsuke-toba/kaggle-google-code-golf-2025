def p(g):
 *C,B=sorted({*sum(g,[])},key=sum(g,[]).count)
 def f(c,h=g):
  while c not in h[0]:h=h[1:]
  h=[*zip(*h[::-1])]
  while c not in h[0]:h=h[1:]
  h=[*zip(*h[::-1])]
  while c not in h[0]:h=h[1:]
  h=[*zip(*h[::-1])]
  while c not in h[0]:h=h[1:]
  h=[*zip(*h[::-1])]
  return [[[B,c][x==c]for x in t]for t in h]
 for c in C:
  for d in C:
   if(c-d)*any(all(f(c)[i+y>>1][j+x>>1]==[B,c][f(d)[y][x]==d]for x in range(len(f(d)[0]))for y in range(len(f(d))))for j in range(len(f(c)[0])*2-len(f(d)[0])+1)for i in range(len(f(c))*2-len(f(d))+1)):return f(c)