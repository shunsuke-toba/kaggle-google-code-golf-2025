def p(g):
 R=range;h=len(g);w=len(g[0])
 _,a,b,c,d,v=max(((c-a+1)*(d-b+1),a,b,c,d,v)for a in R(h)for b in R(w)if(v:=g[a][b])for c in R(a,h)for d in R(b,w)if all(g[x][y]==v for x in R(a,c+1)for y in R(b,d+1)))
 return[[v*(a<=i<=c)*(b<=j<=d)for j in R(w)]for i in R(h)]
