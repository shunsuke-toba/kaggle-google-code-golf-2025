def p(g,L=len,F=filter):
 for _ in 0,1:
  r=0
  while L({*g[r]})<3:r+=1
  a=g[r];s=[*F(None,a)];n=L(s);d=a.index(s[0])
  a[:]=(s*(L(a)//n+2))[-d%n:][:L(a)]
  g=[*map(list,zip(*g))]
 return g

