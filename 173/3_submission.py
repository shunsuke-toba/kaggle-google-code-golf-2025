def p(g):
 w=len(g[0])+2;g=sum(([0,*r,0]for r in g),[0]*w)+[0]*w;P=range(w+1,~w+len(g))
 for j in P:
  for d in 1,w,w+1,w-1:
   if(a:=g[j+d])==g[j-d]>0<(c:=g[j]):
    for k in P:
     if c==g[k]or a==g[k+d]==g[k-d]:g[k-d:k+d+1:d]=a,c,a
 return[g[i:i+w-2]for i in P[::w]]