def p(g):
 w=len(g[0]);t=s=w*len(g);v=[1]*s
 while t:
  t-=1;q=g[t//w][t%w]%9*v[t]*[t];d=v[t]=0
  for j in q:
   for k in j-1,j+1,j-w,j+w:
    if s>k>=0<k%w-j%w+2<4>g[k//w][k%w]:d+=1-2*v[k];q+=v[k]*[k];v[k]=0
  for k in q*d:g[k//w][k%w]=8
 return g