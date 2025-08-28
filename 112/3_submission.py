def p(g):
 w=len(g[0]);s=sum(g,[]);i=s.index(3);Y,X=i//w*2|1,i%w*2|1
 while i:
  if s[i:=i-1]:t=g[Y-i//w];t[i%w]=t[X-i%w]=g[i//w][X-i%w]=2
 return g