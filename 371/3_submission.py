def p(g):
 a=sum(g,[]);y,x=divmod((i:=a.index(1))+a.index(1,i+1)>>1,len(g[0]))
 for k in-1,0,1:g[y+k][x]=g[y][x+k]=3
 return g