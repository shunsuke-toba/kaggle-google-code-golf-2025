def p(g,A=range):
 c=i=a=e=99;b=d=j=0;L=()
 for r in A(len(g)):
  for o,v in enumerate(g[r]):
   if v&4:b=r;d=o;a>r and(a:=r,c:=o)
   elif v*(a<b<=r):e=min(e,r);i=min(i,o);f=r-e+1;j=max(j,o-i+1)
   elif v:L+=(r,o,v),
 for k in A(5):
  for r in A(a,b):
   for o in A(c,d):
    try:
     for x,y,z in L:1/(g[e+(x-r)//k][i+(y-o)//k]==z)
     for q in A(f*k):g[r+q][o:o+j*k]=[g[e+q//k][i+p//k]for p in A(j*k)]
     return[r[c:d+1]for r in g[a:b+1]]
    except:0