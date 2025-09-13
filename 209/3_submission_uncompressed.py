def p(g,R=range,E=enumerate):
 i=a=e=99;j=0;l=()
 for r,y in E(g):
  for o,v in E(y):
   if v&4:b=r;d=o;a>r and(a:=r,c:=o)
   elif v>0<b>a:e=min(e,r);i=min(i,o);h=r-e+1;j=max(j,o-i+1)
   elif v:l+=(r,o,v),
 for k in R(1,5):
  for r in R(a,b):
   for o in R(c,d):
    try:
     for x,y,z in l:[0][g[e+(x-r)//k][i+(y-o)//k]^z]
     for x in R(h*k):g[r+x][o:o+j*k]=[g[e+x//k][i+y//k]for y in R(j*k)]
     return[r[c:d+1]for r in g[a:b+1]]
    except:0