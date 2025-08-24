def p(g):
 c=[*filter(any,zip(*g))];r=[[0]*len(c)for _ in g];o=e=i=0
 while c:
  j=1
  while c[j:]and 5 not in c[j]:j+=1
  s,c=c[:j+1],c[j+1:];d=sum({*sum(s,())})-5;o+=(s[0]+(5,)).index(5)%3-e;e=(s[-1]+(5,)).index(5)%3
  for t in s:
   for y in 0,1,2:r[(y-o)%3][i]=t[y]and d
   i+=1
 return r
