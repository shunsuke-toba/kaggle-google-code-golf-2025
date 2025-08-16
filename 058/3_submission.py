def p(g):
 n=len(g);o=[[0]*n for _ in g];o[0]=[3]*n;x=n-1;y=0;u=(1,0,-1,0);a=n-1;i=1
 while a>0:
  for _ in 0,1:
   dx=u[i];dy=u[i-1]
   for _ in[0]*a:y+=dy;x+=dx;o[y][x]=3
   i=(i+1)%4
  a-=2
 return o
