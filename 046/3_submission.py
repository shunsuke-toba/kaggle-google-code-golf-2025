def p(g):
 c=[*filter(any,zip(*g))];r=[[],[],[]];o=e=3
 while c:
  j=1
  while c[j:]and(5in c[j])<1:j+=1
  s,c=c[:j+1],c[j+1:];d=sum({*sum(s,())})-5;o+=(*s[0],5).index(5)-e;e=(*s[-1],5).index(5)
  for y in 0,1,2:r[y-o%3]+=[t[y]and d for t in s]
 return r