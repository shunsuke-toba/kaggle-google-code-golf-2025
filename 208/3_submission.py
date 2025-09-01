def p(g):
 f=sum(g,[]);c=f.count;k=min(f,key=c);a,x=divmod(f.index(k),21);w=g[a].count(k);h=c(k)//2+2-w;i=j=0
 while g[i][j]==k or sum(sum(R[j+1:j+w-1])for R in g[i+1:i+h-1]):j+=1;j%=22-w;i+=j<1
 while h:h-=1;g[i+h][j:j+w]=g[a+h][x:x+w]
 return g