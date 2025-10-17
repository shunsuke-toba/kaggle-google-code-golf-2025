def p(m):
 import re;i=sum(m,[]);e=i.count;b=max(i,key=e);u=[]
 for r in{*i}-{b}:
  i=str(r);l=1|2*(e(r)>1);y=l,r,l
  for k in range(112):o=k//28+2;t=k%7+1;y=any(re.search(i*o+f"[^{i}]"*t+i,str(r)[1::3])for r in m)and(2*o+t,r,o)or y;m=[*map(list,zip(*m[::-1]))]
  u+=y,
 c=max(u)[0];m=[[b]*c for _ in range(c)]
 for s,r,o in u:
  for k in range(o):m[i:=c-s>>1][i+k]=m[i+k][i]=r
  m=[*map(list,zip(*m[::-1]))]
  for k in range(o):m[i:=c-s>>1][i+k]=m[i+k][i]=r
  m=[*map(list,zip(*m[::-1]))]
  for k in range(o):m[i:=c-s>>1][i+k]=m[i+k][i]=r
  m=[*map(list,zip(*m[::-1]))]
  for k in range(o):m[i:=c-s>>1][i+k]=m[i+k][i]=r
  m=[*map(list,zip(*m[::-1]))]
 return m