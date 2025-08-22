def p(g):
 n=len(g);R=range(n)
 f=lambda x,y,v:0if(x%n-x|y%n-y)or(x,y)in v or g[x][y]-5else v.add((x,y))or 1+f(x+1,y,v)+f(x-1,y,v)+f(x,y+1,v)+f(x,y-1,v)
 return[[(g[i][j]&1)+(f(i,j,set())==6)for j in R]for i in R]