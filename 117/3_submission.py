def p(g):
 w=len(g);f=sum(g,[]);k=b=~0
 while(f[k+~w]==f[k-w+1]==f[k+w-1]==f[k-~w]>0)<1:k-=1
 for v in f:
  b+=1;m=2*k-b
  if v:g[y:=m//w+w][b%w]=g[y][m%w]=g[b//w][m%w]=v
 return g