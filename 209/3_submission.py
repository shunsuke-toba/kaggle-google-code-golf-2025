def p(g,R=range,E=enumerate):
 i=a=e=99;j=0;L=()
 for r,h in E(g):
  for o,v in E(h):
   if v&4:b=r;d=o;a>r and(a:=r,c:=o)
   elif v>0<b>a<r:e=min(e,r);i=min(i,o);f=r-e+1;j=max(j,o-i+1)
   elif v:L+=(r,o,v),
 for k in R(5):
  for r in R(a,b):
   for o in R(c,d):
    try:
     for x,y,z in L:[0][g[e+(x-r)//k][i+(y-o)//k]^z]
     for q in R(f*k):g[r+q][o:o+j*k]=[g[e+q//k][i+p//k]for p in R(j*k)]
     return[r[c:d+1]for r in g[a:b+1]]
    except:0