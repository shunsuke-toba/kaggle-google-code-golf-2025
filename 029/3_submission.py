def p(g):
 b=bytes(sum(g,[]));w=len(g[0])
 for k in b:
  n=b.find(k);m=b.rfind(k)
  if{*b[n:n+m%w-n%w]+b[n:m:w]}<={k}:return[r[n%w+1:m%w]for r in g[n//w+1:m//w]]