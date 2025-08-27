def p(g):
 w=len(g);f=sum(g,[])
 for k in range(~w+w*w):
  if 0<f[k]==f[k+~w]==f[k-w+1]==f[k+w-1]==f[k-~w]:a=k//w*2;b=k%w*2
 for k,v in enumerate(f):
  if v:g[r:=k//w][b-(c:=k%w)]=g[a-r][c]=g[a-r][b-c]=v
 return g