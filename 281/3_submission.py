p=lambda g:exec('''a=d=0;l=[];e=enumerate
for y,r in e(g):
 for x,p in e(r):
  if p:l or(c:=x);a=a or~y;b=y;d=max(d,x);l+={p}-{8,*l}
y=~a
while b>=y:
 x=c
 while d>=x:g[y][x]=l[~a<y<b>=c<x<d];x+=1
 y+=1''')or g