def p(a):
 h,w=len(a),len(a[0]);R=range
 r,c=zip(*[(i,j)for i in R(h)for j in R(w)if a[i][j]])
 k=a[r[0]][c[0]];y,x=min(r),min(c);Y,X=max(r),max(c);d=(Y-y)//2
 while 1:
  for j in R(x,X+1):
   for b in y,Y:
    if h>b>-1<j<w:a[b][j]=k
  for i in R(y,Y+1):
   for b in x,X:
    if w>b>-1<i<h:a[i][b]=k
  y-=d;Y+=d;x-=d;X+=d
  if y<0>x and Y>=h<=X>=w:break
 return a
