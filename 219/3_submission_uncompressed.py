def p(g):
 b=[*map(any,g)];f=b.index(1);i=b.index(0,f);a=i-f
 while i<14:
  i+=1;u=a+1
  if b[i]:
   while b[i]:i+=1;u-=1
   for x in range(9):
    s=x%u+i-a;w=m=s>g[1][3]>a*3>g[7][7]>g[1][4]
    for q in range(100):k=q%10;o=q%9%a;g[12][q%6+4]|=q%2<w;m|=g[s+o][k]>1>g[f+o][k-x//u]<=k-x//u;g[s+o][k]|=g[f+o][k-x//u]>1>m==g[s+o][k]<=k-x//u<50<q
    if~-m:break
 return g
