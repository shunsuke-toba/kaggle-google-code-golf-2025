def p(g):
 R=range;s=sum(g,[]);A,B={c for c in s if c};f=[A,B][s.count(A)<s.count(B)];o=A+B-f;h=len(g);w=len(g[0]);m=0
 for y in R(h):
  r=g[y]
  for x in R(w):
   if r[x]==f:
    X=x
    while X<w and r[X]==f:X+=1;Y=y
    while Y<h and g[Y][x]==f:Y+=1
    if(u:=(Y-y)*(X-x))>m:m=u;a,b,c,d=y,x,Y,X
 return[[o]*(w:=d-b)]+[[o]+[o*(g[y][x]==o)for x in R(b+1,d-1)]+[o]for y in R(a+1,c-1)]+[[o]*w]
