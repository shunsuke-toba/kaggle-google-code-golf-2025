p=lambda g:exec('''a=c=99;d=0;p=[];e=enumerate
for y,r in e(g):
 for x,k in e(r):
  if k:a=min(a,b:=y);c=min(c,x);d=max(d,x);p+=({k}-{8,*p})
for y in range(a,b+1):
 for x in range(c,d+1):g[y][x]=p[(a<y<b)&(c<x<d)]''')or g