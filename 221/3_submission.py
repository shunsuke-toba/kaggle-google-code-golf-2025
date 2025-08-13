def p(g):
 A=range(9)
 z=n=0
 for b in A:
  if g[b//3][b%3]:n+=1
  else:z+=1
 s=z*3;o=[[0]*s for _ in range(s)];p=0
 m=s//3
 for a in range(m*m):
  i,j=a//m,a%m
  for b in A:
   if p<n:o[i*3+b//3][j*3+b%3]=g[b//3][b%3]
  p+=1
 return o