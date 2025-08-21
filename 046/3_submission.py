def p(g):
 c=[*filter(any,zip(*g))];r=[[]for _ in g];o=e=0
 while c:
  j=1
  while j<len(c)and 5 not in c[j]:j+=1
  k=j+(j<len(c));s=c[:k];c=c[k:]
  d=next(v for t in s for v in t if v%5)
  if r[0]:o+=s[0].index(5)-e
  e=5 in s[-1]and s[-1].index(5)
  for t in s:
   for x in r:x+=0,
   for y,v in enumerate(t):
    if v:r[y-o][-1]=d
 return r
