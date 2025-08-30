def p(g):
 w=len(g[0]);s=sum(g,[]);i=j=s.index(3)
 while i:
  if s[i:=i-1]:t=g[j//w*2+1-i//w];t[X:=j%w*2+1-i%w]=g[i//w][X]=t[i%w]=2
 return g