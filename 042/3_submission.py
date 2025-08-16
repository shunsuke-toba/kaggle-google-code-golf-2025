def p(g):
 d={}
 for k in range(100):
  i=k//10;j=k%10;r=g[i]
  if r[j]==3>g[i-1][j]*(i>0)and 3>r[j-1]*(j>0):
   n=1
   while r[j+n:j+n+1]==[3]:n+=1
   d[i,j]=n
 for (i,j),n in d.items():
  for s in 1,-1:
   if(i-n,j-s*n)not in d and(i+n,j+s*n)in d:
    a=i;b=j
    while(a+n,b+s*n)in d:a+=n;b+=s*n
    for u in range(n*n):
     for P,Q in((i-n+u//n,b+s*n+u%n),(a+n+u//n,j-s*n+u%n)):
      if-1<P<10>Q>-1:g[P][Q]=8
    break
 return g
