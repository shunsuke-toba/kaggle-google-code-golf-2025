def p(g):
 s=sum(g,[]);w=len(g[0])
 for k in s:
  n=s.index(k);m=len(s)+~s[::-1].index(k);a=n//w;b=m//w;c=n%w;u=m%w-c
  if{k}=={*(s[n:n+u+1]+s[m-u:m+1]+s[n:m+1:w]+s[n+u:m+1:w])}:return[r[c+1:c+u]for r in g[a+1:b]]