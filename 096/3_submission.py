def p(g):
 import re
 r=range
 f=sum(g,[]);b=max(f,key=f.count)
 t=lambda m:[*map(list,zip(*m[::-1]))]
 L=[]
 for x in{*f}-{b}:
  s=str(x);y=()
  for w in r(2,9):
   for d in r(1,15):
    for _ in r(4):
     if any(re.search(s*w+f"[^{s}]"*d+s,"".join(map(str,r)))for r in g):y=(2*w+d,x,w)
     g=t(g)
  L+=y or ((1,x,1),(3,x,3))[f.count(x)>1],
 L.sort();z=L[-1][0]
 o=[[b]*z for _ in r(z)]
 for i in r(len(L)):
  _,x,w=L[~i]
  for _ in r(4):
   for k in r(w):o[i][i+k]=o[i+k][i]=x
   o=t(o)
 return o
