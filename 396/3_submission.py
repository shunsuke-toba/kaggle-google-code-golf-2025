def p(g):
 s=sum(g,[]);o,f=sorted({*s}-{0},key=s.count);a=b=w=0
 for j,r in enumerate(g):
  t=bytes(x==f for x in r)
  for e in t.split(b'\0'):
   if (d:=len(e))>w:a=j;b=t.find(e);w=d
 c=a
 while c<len(g)and g[c][b]==f:c+=1
 t=[[o]*w];return t+[[o,*r[b+1:b+w-1],o]for r in g[a+1:c-1]]+t
