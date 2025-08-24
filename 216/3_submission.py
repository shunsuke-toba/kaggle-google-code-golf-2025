def p(g):
 b=o=0
 for n in range(400):
  i=n//20;j=n%20;r=0;a=[];y=i
  while y<20>g[y][j]>0:s=g[y][j:]+[0];x=s.index(0);t=s[:x];a+=t,;r+=sum(t)-x;g[y][j:j+x]=x*[0];y+=1
  if r>b:o,b=a,r
 return o