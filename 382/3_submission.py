def p(g):
 h=len(g);w=len(g[0]);v=any(2 in(r[0],r[-1])for r in g)
 if v:d=[(r[0]==2)-(r[-1]==2)for r in g];s=[(0,j,1,0)for j in range(w)if g[0][j]>7]+[(h-1,j,-1,0)for j in range(w)if g[-1][j]>7]
 else:d=[(g[0][j]==2)-(g[-1][j]==2)for j in range(w)];s=[(i,0,0,1)for i in range(h)if g[i][0]>7]+[(i,w-1,0,-1)for i in range(h)if g[i][-1]>7]
 for r,c,e,f in s:
  while h>r>=0<=c<w:
   g[r][c]=8;r+=e;c+=f
   if h>r>=0<=c<w:(c:=c+d[r])if v else(r:=r+d[c])
   else:break
 return g
