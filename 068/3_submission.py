def p(g):
 a=sum(g,[]);y,x=divmod(a.index(b:=min(a,key=a.count)),10);g=[10*[0]for _ in g]
 for R in g[y-1:y+2]:R[x-1:x+2]=2,2,2
 g[y][x]=b;return g
