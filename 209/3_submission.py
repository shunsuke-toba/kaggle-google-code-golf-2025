def p(g):
 m=len(g[0]);e=len(g);R=range;A=min;B=max
 a=e;c=i=m;b=d=f=j=0;I=[]
 for t in R(e*m):
  v=g[r:=t//m][o:=t%m]
  if v==4:a=A(a,r);b=B(b,r);c=A(c,o);d=B(d,o)
  elif v and a<b<=r:e=A(e,r);f=B(f,r);i=A(i,o);j=B(j,o)
  elif v:I+=[(r,o,v)]
 h=f-e+1;w=j-i+1
 for k in 2,3,4:
  for r in R(a,b-h*k+2):
   for o in R(c,d-w*k+2):
    try:
     if all(g[e+(R-r)//k][i+(O-o)//k]==V for R,O,V in I):
      for q in R(h*k):g[r+q][o:o+w*k]=[g[e+q//k][i+p//k]for p in R(w*k)]
      return[r[c:d+1]for r in g[a:b+1]]
    except:0