def p(g):
 w=len(g[0]);s=sum(g,[]);i=j=s.index(3)
 while i:
  if s[i:=i-1]:t=g[(k:=2*j+w-i+1)//w];t[k%w]=g[i//w][k%w]=t[i%w]=2
 return g