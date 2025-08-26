def p(g):
 A=min;B=max;a=e=len(g);c=i=m=len(g[0]);b=d=f=j=0;S=I=();Y=range
 for t in Y(e*m):
  if (v:=g[r:=t//m][o:=t%m])==4:a=A(a,r);b=B(b,r);c=A(c,o);d=B(d,o)
  elif v:S+=(r,o,v),
 for r,o,v in S:
  if a<=r<=b and c<=o<=d:I+=(r,o,v),
  else:e=A(e,r);f=B(f,r);i=A(i,o);j=B(j,o)
 h=f-e+1;w=j-i+1
 for k in 2,3,4:
  for r in Y(a,b-h*k+2):
   for o in Y(c,d-w*k+2):
    try:
     if all(g[e+(R-r)//k][i+(O-o)//k]==V for R,O,V in I):
      for q in Y(h*k):g[r+q][o:o+w*k]=[g[e+q//k][i+p//k]for p in Y(w*k)]
      return[r[c:d+1]for r in g[a:b+1]]
    except:0
