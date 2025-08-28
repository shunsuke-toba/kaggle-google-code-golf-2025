def p(g):
 m=len(g[0]);E=len(g);R=range;A=min;B=max
 a=e=E;c=i=m;b=d=f=j=0;L=[]
 for t in R(E*m):
  v=g[r:=t//m][o:=t%m]
  if v==4:a=A(a,r);b=B(b,r);c=A(c,o);d=B(d,o)
  elif v and r>=b>a:e=A(e,r);f=B(f,r);i=A(i,o);j=B(j,o)
  elif v:L+=[(r,o,v)]
 h,w=f-e+1,j-i+1
 for k in 2,3,4:
  for r in R(a,b-h*k+2):
   for o in R(c,d-w*k+2):
    try:
     for x,y,z in L:assert g[e+(x-r)//k][i+(y-o)//k]==z
     for q in R(h*k):g[r+q][o:o+w*k]=[g[e+q//k][i+p//k]for p in R(w*k)]
     return[r[c:d+1]for r in g[a:b+1]]
    except:0