def p(g):
 h,w=len(g),len(g[0])
 for v in{*sum(g,[])}-{0}:
  t=[(r,c)for r in range(h)for c in range(w)if g[r][c]==v]
  if len(t)>3:
   a=min(p[0]for p in t);b=max(p[0]for p in t);c=min(p[1]for p in t);d=max(p[1]for p in t)
   if g[a][c]==v==g[a][d]==g[b][c]==g[b][d]and all(g[a][i]==v==g[b][i]for i in range(c,d+1))and all(g[i][c]==v==g[i][d]for i in range(a,b+1)):return[[g[r][c]for c in range(c+1,d)]for r in range(a+1,b)]