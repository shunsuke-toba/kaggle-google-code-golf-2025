def p(e):
 r=k=13
 u=1
 for t,o in enumerate(e):
  for n,o in enumerate(o):
   if o==4:
    if u:g,i=t,n;u=0
    a,z=t,n
 u=[o[i:z+1]for o in e[g:a+1]]
 for t,o in enumerate(e):
  for n,o in enumerate(o):
   if t-g|a-t|n-i|z-n<0<o:
    if t<r:r=t
    if n<k:k=n;f=o!=u[1][0]
 for t,o in enumerate(u[1:-1]):
  o[1:-1]=e[r+t][k:k+z-i-1][::1-2*f]
 return u