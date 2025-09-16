def p(g):
 w=len(g);f=sum(g,[]);k=b=~0
 while(f[k+~w]==f[k-w+1]==f[k+w-1]==f[k-~w]>0)<1:k-=1
 for v in f:
  b+=1
  if v:g[y:=(m:=2*k-b)//w+w][b%w]=g[y][d:=m%w]=g[b//w][d]=v
 return g