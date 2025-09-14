def p(g):
 w=len(g[0])+2;p=range(w+1,~w+len(g:=sum(([0,*r,0]for r in g),s:=[0]*w)+s))
 for d in w+1,w,w-1,1:
  for j in p:
   if(a:=g[j+d])==g[j-d]>0<(c:=g[j]):
    for j in p:
     if c==g[j]or g[j+d]==g[j-d]==a:g[j-d:j-~d:d]=a,c,a
 return[g[j:j+w-2]for j in p[::w]]