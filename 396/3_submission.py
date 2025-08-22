def p(g):
 R=range;s=sum(g,[]);a,b={*s}-{0};f=max(a,b,key=s.count);o=a+b-f;m=0
 for y,r in enumerate(g):
  for x in R(len(r)):
   if r[x]==f:
    X=x
    while X<len(r) and r[X]==f:X+=1;Y=y
    while Y<len(g) and g[Y][x]==f:Y+=1
    if(u:=(Y-y)*(X-x))>m:m=u;a,b,c,d=y,x,Y,X
 w=d-b
 return[[o]*w]+[[o,*[o*(g[y][x]==o)for x in R(b+1,d-1)],o]for y in R(a+1,c-1)]+[[o]*w]
