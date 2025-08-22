def p(g):
 import re
 R=range
 f=sum(g,[])
 b=max(f,key=f.count)
 I=[]
 for x in set(f):
  if x==b:continue
  s=None
  for w in R(2,9):
   for d in R(1,15):
    for _ in R(4):
     if any(re.search(str(x)*w+f"[^{x}]"*d+str(x),"".join(map(str,r)))for r in g):s=w,d
     g=[list(r)for r in zip(*g[::-1])]
  if not s:s=(1,-1) if f.count(x)==1 else (3,-3)
  I+=[(x,*s)]
 I.sort(key=lambda t:t[1]*2+t[2])
 z=I[-1][1]*2+I[-1][2]
 o=[[b]*z for _ in R(z)]
 i=0
 while I:
  x,w,d=I.pop()
  for _ in R(4):
   for k in R(w):o[i][i+k]=o[i+k][i]=x
   o=[list(r)for r in zip(*o[::-1])]
  i+=1
 return o
