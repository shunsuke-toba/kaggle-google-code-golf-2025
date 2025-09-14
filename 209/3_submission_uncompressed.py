def p(g):
 i=a=e=99;j=0;l=()
 for R,y in enumerate(g):
  for O,v in enumerate(y):
   if v&4:b=R;d=O;a>R and(a:=R,c:=O)
   elif v>0<b>a:e=min(e,R);i=min(i,O);h=R-e+1;j=max(j,O-i+1)
   elif v:l+=(R,O,v),
 for k in range(1,5):
  for R in range(a,b):
   for O in range(c,d):
    try:
     for r,o,v in l:g[e+(r-R)//k][i+(o-O)//k]^v and 1/0
     for r in range(h*k):
      for o in range(j*k):g[R+r][O+o]=g[e+r//k][i+o//k]
     return[R[c:d+1]for R in g[a:b+1]]
    except:0
