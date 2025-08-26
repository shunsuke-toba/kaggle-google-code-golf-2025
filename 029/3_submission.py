def p(g):
 b=bytes(sum(g,[]));w=len(g[0])
 for k in b:
  n=b.find(k);m=b.rfind(k);d=m%w-n%w;t=b[n:m+1]
  if{*t[:d+1]+t[::w]+t[d::w]}<={k}:return[r[n%w+1:m%w]for r in g[n//w+1:m//w]]