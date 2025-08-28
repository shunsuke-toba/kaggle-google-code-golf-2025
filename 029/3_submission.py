def p(g):
 b=bytes(sum(g,[]));w=len(g[0])
 for k in b:
  n=b.find(k);m=b.rfind(k);d=m%w-n%w
  if{*b[n+1:n+d]+b[n:m:w]+b[n+d:m:w]}<={k}:return[r[n%w+1:m%w]for r in g[n//w+1:m//w]]