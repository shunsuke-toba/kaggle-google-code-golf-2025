def p(g,E=enumerate):
 d={}
 for i,r in E(g):
  for j,v in E(r):
   if v:t=d.setdefault(v,[i,i,j,j]);t[1]=i;t[3]=j
 a,b=d.values();C=lambda x,y:y[2]<=x[2]<x[3]<=y[3];H=C(a,b)|C(b,a)
 if~-H:g=[*map(list,zip(*g))];a=a[2:]+a[:2];b=b[2:]+b[:2]
 I=(a,b)[C(b,a)];L=I[2]+1;U=I[3]
 for r in g[min(a[1],b[1])+1:max(a[0],b[0])]:r[L:U]=[8]*(U-L)
 return~-H and[*map(list,zip(*g))]or g