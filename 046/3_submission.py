f=lambda x:5 in x and x.index(5)
def p(g):
 c=[*filter(any,zip(*g))]
 r=[[0]*len(c)for _ in g]
 o=e=i=0
 while c:
  j=1
  while j<len(c)and 5 not in c[j]:j+=1
  s,c=c[:j+1],c[j+1:];d=max({*sum(s,())}-{0,5})
  o+=f(s[0])-e;e=f(s[-1])
  for t in s:
   for y,v in enumerate(t):
    if v:r[y-o][i]=d
   i+=1
 return r
