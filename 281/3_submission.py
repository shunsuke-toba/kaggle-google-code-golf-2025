p=lambda g:exec('''a=d=y=0;l=[]
for r in g:
 x=0
 for p in r:
  if p:l or(c:=x);a=a or~y;b=y;d=max(d,x);l+={p}-{8,*l}
  x+=1
 y+=1
y=~a
while b>=y:
 x=c
 while d>=x:g[y][x]=l[~a<y<b>=c<x<d];x+=1
 y+=1''')or g