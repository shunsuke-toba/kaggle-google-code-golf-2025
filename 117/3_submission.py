def p(g):
 w=len(g);f=sum(g,[])
 for k in range(~w+w*w):
  if 0<f[k]==f[k+~w]==f[k-w+1]==f[k+w-1]==f[k-~w]:a=k//w;b=k%w
 for k,v in enumerate(f):
  if v:g[r:=k//w][2*b-(c:=k%w)]=g[A:=2*a-r][c]=g[A][2*b-c]=v
 return g
