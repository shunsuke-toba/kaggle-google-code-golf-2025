def p(g):
 b=o=0
 for n in range(400):
  if g[i:=n//20][j:=n%20]:
   x=j;y=i
   while x<20>g[i][x]>0:x+=1
   while y<20>g[y][j]>0:y+=1
   a=[];r=0
   for k in g[i:y]:s=k[j:x];a+=s,;r+=s.count(2);k[j:x]=[0]*(x-j)
   if r>b:o,b=a,r
 return o
