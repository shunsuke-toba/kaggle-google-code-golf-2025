def p(g):
 c=[*filter(any,zip(*g))];r=[[]for _ in g];o=e=0
 while c:
  j=1
  while j<len(c)and 5 not in c[j]:j+=1
  s=c[:j+1];c=c[j+1:]
  d=next(v for t in s for v in t if v%5)
  o+=s[0].count(5)and s[0].index(5)-e
  e=5 in s[-1]and s[-1].index(5)
  for t in s:
   for x in r:x+=0,
   for y,v in enumerate(t):
    if v:r[y-o][-1]=d
 return r
