def p(g):
 f=sum(g,[]);a=f.index(k:=min(f,key=f.count));x=a%21;y=a//21;h,w=divmod(462-f[::-1].index(k)-a,21);i,j=[(i,j)for i in range(22-h)for j in range(22-w)if(j-x|i-y)*all(sum(r[j+1:j+w-1])<1 for r in g[i+1:i+h-1])][0]
 while h:h-=1;g[i+h][j:j+w]=g[y+h][x:x+w]
 return g