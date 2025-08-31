p=lambda g:exec('''a=c=99;d=0;p=[];e=enumerate
for y,r in e(g):
 for x,k in e(r):
  if k:a=min(a,b:=y);c=min(c,x);d=max(d,x);p+=({k}-{8,*p})
y=a
while y<=b:
 x=c
 while x<=d:g[y][x]=p[(a<y<b)&(c<x<d)];x+=1
 y+=1''')or g