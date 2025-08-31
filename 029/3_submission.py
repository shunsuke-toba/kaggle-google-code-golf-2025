def p(g):
 b=bytes(sum(g,[]));w=len(g[0])
 for k in b:
  if{*b[(n:=b.find(k)):(m:=b.rfind(k))%w-n%w]+b[n:m:w]}<={k}:return[r[n%w+1:m%w]for r in g[n//w+1:m//w]]