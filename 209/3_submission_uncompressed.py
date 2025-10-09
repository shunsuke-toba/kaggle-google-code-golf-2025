def p(g):
 i=a=e=99;l=m=()
 for y,Y in enumerate(g):
  for x,v in enumerate(Y):
   if v&4:b=y;d=x;a>y and(a:=y,c:=x)
   elif v>0<b>a:m+=(y,x,v),
   elif v:l+=(y,x,v),
 for y,x,v in m:e=min(e,y);i=min(i,x)
 for k in range(1,5):
  for Y in range(a,b):
   for X in range(c,d):
    try:
     for y,x,v in l:1/(g[e+(y-Y)//k][i+(x-X)//k]==v)
     for y,x,v in m:
      for r in range(k):
       for o in range(k):g[Y+(y-e)*k+r][X+(x-i)*k+o]=v
     return[g[Y][c:d+1]for Y in range(a,b+1)]
    except:0