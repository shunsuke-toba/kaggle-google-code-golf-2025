def p(g):
 n=len(g);m=len(g[0]);a=n;c=m;b=d=0;S=[]
 for t in range(n*m):
  if (v:=g[r:=t//m][o:=t%m])==4:a=min(a,r);b=max(b,r);c=min(c,o);d=max(d,o)
  elif v:S+=(r,o),
 e=n;f=0;i=m;j=0;I=[]
 for r,o in S:
  if a<=r<=b and c<=o<=d:I+=(r,o),
  else:e=min(e,r);f=max(f,r);i=min(i,o);j=max(j,o)
 h=f-e+1;w=j-i+1
 for k in 2,3,4:
  H=h*k;W=w*k
  for R in range(a,b-H+2):
   for O in range(c,d-W+2):
    try:
     if all(g[e+(r-R)//k][i+(o-O)//k]==g[r][o]for r,o in I):
      for q in range(H):g[R+q][O:O+W]=[g[e+q//k][i+p//k]for p in range(W)]
      return[r[c:d+1]for r in g[a:b+1]]
    except:0
