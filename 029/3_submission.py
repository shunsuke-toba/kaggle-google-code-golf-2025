def p(g):
 s=sum(g,[]);w=len(g[0])
 for k in s:
  n=s.index(k);m=len(s)+~s[::-1].index(k);a=n//w;b=m//w;c=n%w;d=m%w
  if{k}=={*(g[a][c:d+1]+g[b][c:d+1]+[r[e]for r in g[a:b+1]for e in(c,d)])}:return[r[c+1:d]for r in g[a+1:b]]