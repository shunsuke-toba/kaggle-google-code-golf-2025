def p(g):
 n=len(g);R=range(n)
 def f(x,y,v):return 0if((x,y)in v)|~-(n>x>=0<=y<n)or g[x][y]-5else v.add((x,y))or 1+f(x+1,y,v)+f(x-1,y,v)+f(x,y+1,v)+f(x,y-1,v)
 return[[(g[i][j]&1)+(f(i,j,set())==6)for j in R]for i in R]