def p(g):
 f=i=[*map(any,g)].index(1)
 while any(g[i]):i+=1;a=i-f
 while i<14:
  i+=1;u=a+1
  if any(g[i]):
   while any(g[i]):i+=1;u-=1
   for x in range(9):
    t=x//u;s=x%u+i-a;w=m=s>g[1][3]>a*3>g[7][7]>g[1][4]
    for j in range(60):k=j%10;p=j//10%a;g[12][j%6+4]|=j%2<w;m|=g[s+p][k]>1>g[f+p][k-t]<=k-t;g[s+p][k]|=g[f+p][k-t]>1>m==g[s+p][k]<=k-t<30<=j
    if~-m:break
 return g
