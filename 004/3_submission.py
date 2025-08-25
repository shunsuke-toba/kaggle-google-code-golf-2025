def p(g):
 d={}
 for r in g[::-1]:
  j=len(r)
  while j:
   if v:=r[j:=j-1]:d[v]=R,c=d.get(v,(r,j));r[j]=0;r[j+(r!=R)*(j<c)]=v
 return g
