def p(g):
 R=range;n=len(g);m=len(g[0]);P=n;Q=m;b=n*m;D={}
 for p in R(1,n+1):
  for q in R(1,m+1):
   d={}
   if p*q<b and all((v:=g[i][j])<1 or d.setdefault((i%p,j%q),v)==v for i in R(n) for j in R(m)):P,Q,b,D=p,q,p*q,d
 return[[D[i%P,j%Q]for j in R(m)]for i in R(n)]
