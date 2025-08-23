def p(g):
 s=sum(g,[]);a,b={*s}-{0};f=max(a,b,key=s.count);o=a+b-f;a=b=w=0
 for j,r in enumerate(g):
  t=''.join('01'[x==f]for x in r);i=0
  for e in t.split('0'):
   if(d:=len(e))>w:a=j;b=i;w=d
   i+=d+1
 c=a
 while c<len(g)and g[c][b]==f:c+=1
 return[[o]*w]+[[o,*r[b+1:b+w-1],o]for r in g[a+1:c-1]]+[[o]*w]
