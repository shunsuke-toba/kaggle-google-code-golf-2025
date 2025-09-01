def p(g):
 import re;r=range;b=max(f:=sum(g,[]),key=f.count);t=lambda m:[*map(list,zip(*m[::-1]))];L=[]
 for x in{*f}-{b}:
  s=str(x);c=2*(f.count(x)>1)+1;y=c,x,c
  for n in r(28):
   for _ in r(4):w=n//7+2;d=n%7+1;y=any(re.search(s*w+f"[^{s}]"*d+s,str(R)[1::3])for R in g)and(2*w+d,x,w)or y;g=t(g)
  L+=y,
 m=max(L)[0];o=[[b]*m for _ in r(m)]
 for z,x,w in L:
  i=m-z>>1
  for _ in r(4):
   for k in r(w):o[i][i+k]=o[i+k][i]=x
   o=t(o)
 return o