def p(g):
 f=sum(g,[])
 a,x=divmod(f.index(k:=min(f,key=f.count)),21);h=f[x::21].count(k);w=g[a].count(k);i=j=t=0
 while g[i][j]==k or sum(sum(R[j+1:j+w-1])for R in g[i+1:i+h-1]):t+=1;i,j=divmod(t,22-w)
 for k in range(h):g[i+k][j:j+w]=g[a+k][x:x+w]
 return g