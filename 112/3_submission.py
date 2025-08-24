def p(g):
 w=len(g[0]);s=sum(g,[]);i=s.index(3);Y,X=i//w*2|1,i%w*2|1;i=0
 for c in s:
  r=i//w;x=i%w;i+=1
  if c%3:g[r][X-x]=g[Y-r][x]=g[Y-r][X-x]=2
 return g
