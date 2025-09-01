def p(g):
 w=len(g);f=sum(g,[]);k=w*w-w-2
 while(f[k]==f[k+~w]==f[k-w+1]==f[k+w-1]==f[k-~w]>0)<1:k-=1
 for b,v in enumerate(f):
  if v:g[y:=k//w*2-b//w][b%w]=g[y][d:=k%w*2-b%w]=g[b//w][d]=v
 return g