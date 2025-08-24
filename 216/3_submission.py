def p(g):
 b=o=0
 for n in range(400):
  i=n//20;j=n%20;x=(g[i][j:]+[0]).index(0);r=0;a=[];y=i
  while y<20>g[y][j]>0:a+=g[y][j:j+x],;r+=a[-1].count(2);g[y][j:j+x]=x*[0];y+=1
  if r>b:o,b=a,r
 return o