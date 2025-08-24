def p(g):
 b=bytes(sum(g,[]));w=len(g[0])
 for k in b:
  n=b.find(k);m=b.rfind(k);u=m%w-n%w;s=b[n:m+1]
  if{k}=={*(s[:u+1]+s[-u-1:]+s[::w]+s[u::w])}:return[r[n%w+1:m%w]for r in g[n//w+1:m//w]]