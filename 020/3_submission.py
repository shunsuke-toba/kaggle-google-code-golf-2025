L=len
R=range
def p(g):
 h=L(g);w=L(g[0]);m=-1;r=c=0
 for i in R(h):
  for j in R(w):
   if g[i][j]:
    v=0;a=i-1;b=j-1
    if a>=0 and b>=0 and a+2<h and b+2<w and g[a][b]and g[a][b+2]and g[a+2][b]and g[a+2][b+2]:v+=1
    a=i-2;b=j
    if a>=0 and a+4<h and b-2>=0 and b+2<w and g[a][b]and g[a+4][b]and g[i][b-2]and g[i][b+2]:v+=2
    if v>m:m=v;r=i;c=j
 for i in R(h):
  for j in R(w):
   v=g[i][j]
   if v:
    y=i-r;x=j-c
    for Y,X in((y,x),(-x,y),(-y,-x),(x,-y)):
     I=r+Y;J=c+X
     if 0<=I<h and 0<=J<w and g[I][J]==0:g[I][J]=v
 return g
