def p(g):
 h,w=len(g),len(g[0]);r=[*map(list,g)]
 def d(i,j):
  if-1<i<h and-1<j<w and g[i][j]==1:
   g[i][j]=2;return[(i,j)]+d(i-1,j)+d(i+1,j)+d(i,j-1)+d(i,j+1)
  return[]
 for k in range(h*w):
  if c:=d(k//w,k%w):
   A,B=zip(*c);a=min(A);b=max(A);e=min(B);f=max(B);F=max(max(x[e:f+1])for x in r[a:b+1])
   for i in range(a-(a>0),b+1):r[i][e:f+1]=[F]*(f-e+1)
   for i,j in c:r[i][j]=1
 return r
