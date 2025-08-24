def p(g):
 w=len(g);f=sum(g,[])
 for k in range(w+1,~w+len(f)):
  if f[k]==f[k+~w]==f[k-w+1]==f[k+w-1]==f[k-~w]>0:a=k//w;b=k%w
 for k,v in enumerate(f):
  if v:c=k%w;g[r:=k//w][2*b-c]=g[A:=2*a-r][c]=g[A][2*b-c]=v
 return g
