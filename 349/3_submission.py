def p(g):
 h=len(g);w=len(g[0]);R=range;S=[]
 for i in R(h):
  for j in R(w):
   if g[i][j]==9 and (i<1 or g[i-1][j]-9) and (j<1 or g[i][j-1]-9):
    x=i
    while x<h and g[x][j]==9:x+=1
    y=j
    while y<w and g[i][y]==9:y+=1
    S+=[(i,x,j,y)]
 for a,b,c,d in S:
  for x in R(c,d):
   y=b
   while y<h and g[y][x]<1:g[y][x]=1;y+=1
 for a,b,c,d in S:
  r=max(b-a,d-c)//2
  for y in R(max(0,a-r),min(h,b+r)):
   for x in R(max(0,c-r),min(w,d+r)):
    if g[y][x]-9:g[y][x]=3
 return g
