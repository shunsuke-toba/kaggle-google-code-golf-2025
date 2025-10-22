def p(c):
 a=b=0;r=0,1,2
 while 0in map(sum,(g:=[c[a+e][b:b+3]for e in r])+[*zip(*g)]):
  b=(b+1)%19;a+=b<1
 for d in-4,0,4:
  for z in-4,0,4:
   t=max(c[a+d+e][b+z+j]for e in r for j in r);l,p=a,b
   for j in c:
    l+=d;p+=z
    for e in r:
     for j in r:
      if g[e][j]and-1<l+e<21 and-1<p+j<21:c[l+e][p+j]=t
 return c