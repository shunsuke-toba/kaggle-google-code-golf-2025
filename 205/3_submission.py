def p(g):
 R=range;l=len;E=enumerate;h=l(g);w=l(g[0]);m=0
 for a in R(h):
  for b in R(a+1,h+1):
   for c in R(w):
    for d in R(c+1,w+1):
     if(k:=l({v for r in g[a:b] for v in r[c:d]})==2 and(b-a)*(d-c))>m:m=k;A,B,C,D=a,b,c,d
 o=[r[C:D]for r in g[A:B]];g=[r[:]for r in o];h=B-A;w=D-C
 for i,r in E(o):
  for j,v in E(r):
   if(i and o[i-1][j]==v)|(i<h-1 and o[i+1][j]==v)|(j and r[j-1]==v)|(j<w-1 and r[j+1]==v):continue
   for k in g:k[j]=v
   g[i]=[v]*w
 return g
