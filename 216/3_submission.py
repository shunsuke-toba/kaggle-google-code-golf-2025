def p(g):
 b=o=0
 for n in range(400):
  if g[i:=n//20][j:=n%20]:
   x=j;r=0;a=[];y=i
   while x<20>g[i][x]>0:x+=1
   while y<20>g[y][j]>0:s=g[y][j:x];a+=s,;r+=s.count(2);g[y][j:x]=[0]*(x-j);y+=1
   if r>b:o,b=a,r
 return o
