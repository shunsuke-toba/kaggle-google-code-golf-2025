def p(g):
 i=a=e=99;j=0;l=()
 for y,Y in enumerate(g):
  for x,v in enumerate(Y):
   if v&4:b=y;d=x;a>y and(a:=y,c:=x)
   elif v>0<b>a:e=min(e,y);i=min(i,x);h=y-e+1;j=max(j,x-i+1)
   elif v:l+=(y,x,v),
 for k in range(1,5):
  for y in range(a,b):
   for x in range(c,d):
    try:
     for r,o,v in l:g[e+(r-y)//k][i+(o-x)//k]-v and 1/0
     for r in range(h*k):
      for o in range(j*k):g[y+r][x+o]=g[e+r//k][i+o//k]
     return[g[y][c:d+1]for y in range(a,b+1)]
    except:0