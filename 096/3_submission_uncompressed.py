def p(g):
 import re;f=sum(g,[]);C=f.count;b=max(f,key=C);L=[]
 for R in{*f}-{b}:
  s=str(R);c=1|2*(C(R)>1);y=c,R,c
  for n in range(112):w=n//28+2;d=n%7+1;y=any(re.search(s*w+f"[^{s}]"*d+s,str(R)[1::3])for R in g)and(2*w+d,R,w)or y;g=[*map(list,zip(*g[::-1]))]
  L+=y,
 m=max(L)[0];g=[[b]*m for _ in range(m)]
 for z,R,w in L:
  for k in range(w):g[i:=m-z>>1][i+k]=g[i+k][i]=R
  g=[*map(list,zip(*g[::-1]))]
  for k in range(w):g[i:=m-z>>1][i+k]=g[i+k][i]=R
  g=[*map(list,zip(*g[::-1]))]
  for k in range(w):g[i:=m-z>>1][i+k]=g[i+k][i]=R
  g=[*map(list,zip(*g[::-1]))]
  for k in range(w):g[i:=m-z>>1][i+k]=g[i+k][i]=R
  g=[*map(list,zip(*g[::-1]))]
 return g