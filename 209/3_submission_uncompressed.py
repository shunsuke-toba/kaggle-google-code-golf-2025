def p(g):
 i=a=e=99;l=m=()
 for y,Y in enumerate(g):
  for x,v in enumerate(Y):
   if v&4:b=y;d=x;a>y and(a:=y,c:=x)
   elif v>0<b>a:e=min(e,y);i=min(i,x);m+=(y,x,v),
   elif v:l+=(y,x,v),
 for k in range(1,5):
  for Y in range(a,b):
   for X in range(c,d):
    try:
     for r,o,v in l:g[e+(r-Y)//k][i+(o-X)//k]-v and 1/0
     for r,o,v in m:
      for y in range(k):
       for x in range(k):g[Y+(r-e)*k+y][X+(o-i)*k+x]=v
     return[g[Y][c:d+1]for Y in range(a,b+1)]
    except:0
