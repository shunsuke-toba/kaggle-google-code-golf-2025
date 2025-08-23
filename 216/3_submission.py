def p(g):
 b=o=0
 for n in range(400):
  j=n%20;i=n//20
  if g[i][j]:
   x=j
   while g[i][x:x+1]>[0]:x+=1
   y=i
   while y<20 and g[y][j]:y+=1
   w=x-j;A=[];r=0
   for k in g[i:y]:s=k[j:x];A+=s,;r+=s.count(2);k[j:x]=[0]*w
   if r>b:o=A;b=r
 return o
