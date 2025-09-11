def p(g):
 _=2;b=[*map(any,g)];f=b.index(1);i=b.index(0,f);a=i-f
 while i<14:
  i+=1;u=a+1
  if b[i]:
   while b[i]:i+=1;u-=1
   for x in range(9):
    t=x//u;s=x%u+i-a;w=m=s>g[1][3]>a*3>g[7][7]>g[1][4]
    for j in range(99):k=j%10;p=j%9%a;g[12][j%6+4]|=j%2<w;m|=g[s+p][k]>1>g[f+p][k-t]<=k-t;g[s+p][k]|=g[f+p][k-t]>1>m==g[s+p][k]<=k-t<50<j
    if~-m:break
 return g
