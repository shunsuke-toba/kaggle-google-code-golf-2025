p=lambda g:exec('''a=d=y=0;l=[]
for r in g:
 x=0
 for p in r:
  if p:l or(c:=x);a=a or~y;b=y;d=max(d,x);l+={p}-{8,*l}
  x+=1
 y+=1
y=b
while~a<=y:
 x=c
 while x<=d:g[y][x]=l[~a<y<b>=c<x<d];x+=1
 y-=1''')or g