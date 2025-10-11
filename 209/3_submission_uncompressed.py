def p(g):
 i=e=a=99;l=m=()
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v&4:
    b=y;d=x
    if a>y:a=y;c=x
   elif v>0<b>a:m+=(y,x,v),;e=min(e,y);i=min(i,x)
   elif v:l+=(y,x,v),
 for k in range(1,5):
  for p in range(a,b):
   for q in range(c,d):
    try:
     for y,x,v in l:1/(g[e+(y-p)//k][i+(x-q)//k]==v)
     for y,x,v in m:
      for r in range(k*k):g[p+(y-e)*k+r//k][q+(x-i)*k+r%k]=v
     return[g[p][c:d+1]for p in range(a,b+1)]
    except:0