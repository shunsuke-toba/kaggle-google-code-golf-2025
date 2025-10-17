def p(e):
 i=k=13
 u=1
 for t,v in enumerate(e):
  for l,v in enumerate(v):
   if v==4:
    if u:c,p=t,l;u=0
    a,d=t,l
 u=[v[p:d+1]for v in e[c:a+1]]
 for t,v in enumerate(e):
  for l,v in enumerate(v):
   if t-c|a-t|l-p|d-l<0<v:
    if t<i:i=t
    if l<k:k=l;o=v!=u[1][0]
 for v in u[1:-1]:
  i+=1;v[1:-1]=e[i-1][k:k+d-p-1][::1-2*o]
 return u