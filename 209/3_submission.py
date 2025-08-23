def p(g):
 m=len(g[0]);a=e=len(g);c=i=m;b=d=f=j=0;S=I=();Y=range
 for t in Y(e*m):
  if (v:=g[r:=t//m][o:=t%m])==4:a=min(a,r);b=max(b,r);c=min(c,o);d=max(d,o)
  elif v:S+=(r,o),
 for r,o in S:
  if a<=r<=b and c<=o<=d:I+=(r,o),
  else:e=min(e,r);f=max(f,r);i=min(i,o);j=max(j,o)
 h=f-e+1;w=j-i+1
 for k in 2,3,4:
  for R in Y(a,b-h*k+2):
   for O in Y(c,d-w*k+2):
    try:
     if all(g[e+(r-R)//k][i+(o-O)//k]==g[r][o]for r,o in I):
      for q in Y(h*k):g[R+q][O:O+w*k]=[g[e+q//k][i+p//k]for p in Y(w*k)]
      return[r[c:d+1]for r in g[a:b+1]]
    except:0
