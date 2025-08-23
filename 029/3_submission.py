def p(g):
 s=sum(g,[]);w=len(g[0])
 for k in s:
  n=s.index(k);m=len(s)+~s[::-1].index(k);u=m%w-n%w
  if{k}=={*(s[n:n+u+1]+s[m-u:m+1]+s[n:m+1:w]+s[n+u:m+1:w])}:return[r[n%w+1:m%w]for r in g[n//w+1:m//w]]