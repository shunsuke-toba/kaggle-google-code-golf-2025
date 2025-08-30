def p(g):
 w=len(g);f=sum(g,[]);k=w*w-w-2
 while not(f[k]==f[k+~w]==f[k-w+1]==f[k+w-1]==f[k-~w]>0):k-=1
 a=k//w*2;b=k%w*2
 for k,v in enumerate(f):
  if v:g[r:=k//w][d:=b-k%w]=g[a-r][k%w]=g[a-r][d]=v
 return g