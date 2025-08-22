def p(g):
 from re import search as S
 r=range
 f=sum(g,[]);s=set(f);b=max(s,key=f.count)
 t=lambda m:[*map(list,zip(*m[::-1]))]
 L=[]
 for x in s-{b}:
  s=str(x);y=None
  for w in r(2,9):
   for d in r(1,15):
    for _ in r(4):
     if any(S(s*w+f"[^{s}]"*d+s,"".join(map(str,R)))for R in g):y=2*w+d,x,w
     g=t(g)
  if not y:y=(1,x,1)if f.count(x)==1 else(3,x,3)
  L+=y,
 L.sort()
 z=L[-1][0]
 o=[[b]*z for _ in r(z)]
 for i,(_,x,w) in enumerate(L[::-1]):
  for _ in r(4):
   for k in r(w):o[i][i+k]=o[i+k][i]=x
   o=t(o)
 return o

