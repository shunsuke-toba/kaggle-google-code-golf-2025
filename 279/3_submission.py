def p(g):
 w=len(g[0]);s=w*len(g);v=[1]*s
 for i in range(s):
  if v[i]and g[i//w][i%w]^9:
   v[i]=d=0;q=[i]
   for j in q:
    for k in j-1,j+1,j-w,j+w:
     if 0<=k<s and-2<k%w-j%w<2 and g[k//w][k%w]^9:d+=1-2*v[k];q+=v[k]*[k];v[k]=0
   if d:
    for k in q:g[k//w][k%w]=8
 return g
