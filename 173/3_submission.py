def p(g):
 w=len(g[0])+2;g=sum(([0]+r+[0]for r in g),[0]*w)+[0]*w;P=range(w+1,~w+len(g))
 for j in P:
  for d in 1,w,w+1,w-1:
   if(a:=g[j+d])==g[j-d]>0<(c:=g[j]):
    for k in P:
     if g[k]==c:g[k+d]=g[k-d]=a
     if g[k+d]==g[k-d]==a:g[k]=c
 return[g[i:i+w-2]for i in P[::w]]
