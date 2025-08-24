def p(g):
 s=sum(g,[]);o,f=sorted({*s}-{0},key=s.count)
 w,c,b=max((len(e),-j,t.find(e))for j,r in enumerate(g)for t in[bytes(x==f for x in r)]for e in t.split(b'\0'));a=c=-c
 while g[c:]and g[c][b]==f:c+=1
 return[(h:=[o]*w),*[[o,*r[b+1:b+w-1],o]for r in g[a+1:c-1]],h]
