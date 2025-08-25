def p(g):
 a=e=len(g);c=i=m=len(g[0]);b=d=f=j=0;S=I=();Y=range
 for t in Y(e*m):
  if (v:=g[r:=t//m][o:=t%m])==4:a=min(a,r);b=max(b,r);c=min(c,o);d=max(d,o)
  elif v:S+=(r,o),
 for r,o in S:
  if a<=r<=b and c<=o<=d:I+=(r,o),
  else:e=min(e,r);f=max(f,r);i=min(i,o);j=max(j,o)
 h=f-e+1;w=j-i+1
 for k in 2,3,4:
  for r in Y(a,b-h*k+2):
   for o in Y(c,d-w*k+2):
    try:
     if all(g[e+(R-r)//k][i+(O-o)//k]==g[R][O]for R,O in I):
      for q in Y(h*k):g[r+q][o:o+w*k]=[g[e+q//k][i+p//k]for p in Y(w*k)]
      return[r[c:d+1]for r in g[a:b+1]]
    except:0
