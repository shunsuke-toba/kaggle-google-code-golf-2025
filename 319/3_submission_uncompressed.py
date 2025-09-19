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
   h=f(d);q=f(c)
   if(c-d)*any(all(q[i+y>>1][j+x>>1]==[B,c][h[y][x]==d]for y in range(len(h))for x in range(len(h[0])))for i in range(len(q)*2-len(h)+1)for j in range(len(q[0])*2-len(h[0])+1)):return q