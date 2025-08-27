def p(g):
 f=sum(g,[]);y,x=divmod(a:=f.index(k:=min(f,key=f.count)),21);h,w=divmod(462-f[::-1].index(k)-a,21);R=range;i,j=[(i,j)for i in R(22-h)for j in R(22-w)if(j-x|i-y)*(sum(sum(r[j+1:j+w-1])for r in g[i+1:i+h-1])<1)][0]
 while h:h-=1;g[i+h][j:j+w]=g[y+h][x:x+w]
 return g