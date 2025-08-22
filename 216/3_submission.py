def p(g):
 R=range;b=o=0
 for i in R(20):
  for j in R(20):
   if g[i][j]:
    x=j
    while x<20 and g[i][x]:x+=1
    y=i
    while y<20 and g[y][j]:y+=1
    A=g[i:y];w=x-j;r=sum(k[j:x].count(2)for k in A)
    if r>b:o=[k[j:x]for k in A];b=r
    for k in A:k[j:x]=[0]*w
 return o

