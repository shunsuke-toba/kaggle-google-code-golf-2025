def p(g):
 w=len(g[0]);s=w*len(g);v=[0]*s
 for i in range(s):
  if g[i//w][i%w]^9 and v[i]<1:
   q=[i];v[i]=1;e=0
   for j in q:
    for k in j-1,j+1,j-w,j+w:
     if 0<=k<s and-2<k%w-j%w<2 and g[k//w][k%w]^9:
      e+=1
      if v[k]<1:v[k]=1;q+=k,
   if e>=2*len(q):
    for k in q:g[k//w][k%w]=8
 return g