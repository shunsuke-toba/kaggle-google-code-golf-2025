def p(g):
 i=99;a=99;e=99;j=0;L=()
 for r,h in enumerate(g):
  for o,v in enumerate(h):
   if v&4:b=r;d=o;a>r and(a:=r,c:=o)
   elif v>0<b>a:e=min(e,r);i=min(i,o);f=r-e+1;j=max(j,o-i+1)
   elif v:L+=(r,o,v),
 for k in range(5):
  for r in range(a,b):
   for o in range(c,d):
    try:
     for x,y,z in L:[0][g[e+(x-r)//k][i+(y-o)//k]^z]
     for q in range(f*k):g[r+q][o:o+j*k]=[g[e+q//k][i+p//k]for p in range(j*k)]
     return[r[c:d+1]for r in g[a:b+1]]
    except:0