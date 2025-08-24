def p(g):
 s=sum(g,[]);o,f,_=sorted({*s},key=s.count)
 w,c,b=max((len(e),-j,t.find(e))for j,r in enumerate(g)for t in[bytes(x==f for x in r)]for e in t.split(b'\0'));t=-c
 while g[t:]and g[t][b]==f:t+=1
 return[[o]*w,*[[o,*r[b+1:b+w-1],o]for r in g[-c+1:t-1]],[o]*w]
