def p(g,r=range,l=len):#p
 s=sum(g,[]);*C,B=sorted({*s},key=s.count)
 def f(c,h=g):
  for _ in g*4:
   while c not in h[0]:h=h[1:]
   h=[*zip(*h[::-1])]
  return[[[B,c][x==c]for x in t]for t in h]
 for c in C:
  for d in C:
   m,n=l(h:=f(d)),l(h[0]);q=f(c)
   if(c-d)*any(all(q[i+k//n>>1][j+k%n>>1]^h[k//n][k%n]in[0,c^d]for k in r(m*n))for i in r(l(q)*2-m+1)for j in r(l(q[0])*2-n+1)):
    return q