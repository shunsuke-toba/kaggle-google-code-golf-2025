def p(g):
 w=len(g[0]);s=sum(g,[]);i=s.index(3);Y,X=i//w*2|1,i%w*2|1
 while i:
  if s[i:=i-1]%3:r=i//w;x=i%w;t=g[Y-r];t[x]=t[X-x]=g[r][X-x]=2
 return g