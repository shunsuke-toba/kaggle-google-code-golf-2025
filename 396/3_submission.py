def p(g):
 s=sum(g,[]);o,f,_=sorted({*s},key=s.count);H=len(g[0])+1;b=bytes(i==f for r in g for i in r+[0])
 w=len(e:=max(b.split(b'\0'),key=len));t=b.find(e);u=b.rfind(e);c=t%H
 return[[o]*w,*[[o,*r[c+1:c+w-1],o]for r in g[t//H+1:u//H]],[o]*w]
