def p(g,a=9,b=-9):
 for n in range(100):
  v=g[i:=n//10][j:=n%10]
  if v==5:g[i][j]=0;a=min(a,j-i);b=max(b,j-i)
  elif v:c=v;d=j-i
 for e in[b+2]*(b>d)+[a-2]*(a<d):
  for i in range(10):
   if-1<i+e<10:g[i][i+e]=c
 return g
