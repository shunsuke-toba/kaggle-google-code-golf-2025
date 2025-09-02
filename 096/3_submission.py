def p(g):
 import re;r=range;f=sum(g,[]);C=f.count;b=max(f,key=C);t=lambda m:[*map(list,zip(*m[::-1]))];L=[]
 for x in{*f}-{b}:
  s=str(x);c=1+2*(C(x)>1);y=c,x,c
  for n in r(112):w=n//28+2;d=n//4%7+1;y=any(re.search(s*w+f"[^{s}]"*d+s,str(R)[1::3])for R in g)and(2*w+d,x,w)or y;g=t(g)
  L+=y,
 m=max(L)[0];o=[[b]*m for _ in r(m)]
 for z,x,w in L:
  for _ in r(4):
   for k in r(w):o[i:=m-z>>1][i+k]=o[i+k][i]=x
   o=t(o)
 return o