def p(g):
 w=len(g[0]);s=w*len(g);v=[1]*s
 for i in range(s):
  if v[i]>0<g[i//w][i%w]^9:
   q=[i];v[i]=d=0
   for j in q:
    for k in j-1,j+1,j-w,j+w:
     if s>k>=0<k%w-j%w+2<4 and g[k//w][k%w]^9:d+=1-2*v[k];q+=v[k]*[k];v[k]=0
   for k in q*d:g[k//w][k%w]=8
 return g
