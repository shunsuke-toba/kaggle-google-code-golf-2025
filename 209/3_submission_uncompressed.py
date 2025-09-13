def p(g):
 i=a=e=99;j=0;l=()
 for r,y in enumerate(g):
  for o,v in enumerate(y):
   if v&4:b=r;d=o;a>r and(a:=r,c:=o)
   elif v>0<b>a:e=min(e,r);i=min(i,o);h=r-e+1;j=max(j,o-i+1)
   elif v:l+=(r,o,v),
 for k in 1,2,3,4:
  for r in range(a,b):
   for o in range(c,d):
    try:
     for x,y,z in l:[0][g[e+(x-r)//k][i+(y-o)//k]^z]
     for x in range(h*k):g[r+x][o:o+j*k]=[g[e+x//k][i+y//k]for y in range(j*k)]
     return[r[c:d+1]for r in g[a:b+1]]
    except:0