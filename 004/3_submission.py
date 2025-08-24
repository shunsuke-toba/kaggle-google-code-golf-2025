def p(g):
 d={}
 for r in g[::-1]:
  for j in range(len(r))[::-1]:
   if v:=r[j]:
    R,c=d.setdefault(v,(r,j))
    r[j]=0;r[j+(r!=R)*(j<c)]=v
 return g
