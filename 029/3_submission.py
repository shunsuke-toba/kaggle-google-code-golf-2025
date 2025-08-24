def p(g):
 b=bytes(sum(g,[]));w=len(g[0])
 for k in b:
  n=b.find(k);m=b.rfind(k);u=m%w-n%w
  if{k}=={*(b[n:n+u+1]+b[m-u:m+1]+b[n:m+1:w]+b[n+u:m+1:w])}:return[r[n%w+1:m%w]for r in g[n//w+1:m//w]]