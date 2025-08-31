def p(g):
 w=len(g);f=sum(g,[]);k=w*w-w-2
 while(f[k]==f[k+~w]==f[k-w+1]==f[k+w-1]==f[k-~w]>0)<1:k-=1
 a=k//w*2
 for b,v in enumerate(f):
  if v:g[r:=b//w][d:=(k%w*2)-b%w]=g[a-r][b%w]=g[a-r][d]=v
 return g