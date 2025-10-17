def p(u):
 *n,B=sorted({*sum(u,[])},key=sum(u,[]).count)
 def f(c,h=u):
  while c not in h[0]:h=h[1:]
  h=[*zip(*h[::-1])]
  while c not in h[0]:h=h[1:]
  h=[*zip(*h[::-1])]
  while c not in h[0]:h=h[1:]
  h=[*zip(*h[::-1])]
  while c not in h[0]:h=h[1:]
  h=[*zip(*h[::-1])]
  return [[[B,c][t==c]for t in t]for t in h]
 for c in n:
  for d in n:
   if(c-d)*any(all(f(c)[i+y>>1][j+t>>1]==[B,c][f(d)[y][t]==d]for t in range(len(f(d)[0]))for y in range(len(f(d))))for j in range(len(f(c)[0])*2-len(f(d)[0])+1)for i in range(len(f(c))*2-len(f(d))+1)):return f(c)