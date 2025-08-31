p=lambda g:exec('''a=c=9;d=0;l=[];e=enumerate
for y,r in e(g):
 for x,p in e(r):
  if p:a=min(a,b:=y);c=min(c,x);d=max(d,x);l+={p}-{8,*l}
y=a
while y<=b:
 x=c
 while x<=d:g[y][x]=l[(a<y<b)&(c<x<d)];x+=1
 y+=1''')or g