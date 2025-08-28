def p(g):
 m=len(g[0]);R=range;A=min;B=max;a=e=99;c=i=m;b=d=f=j=0;L=[]
 for t in R(len(g)*m):
  v=g[r:=t//m][o:=t%m]
  if v==4:a=A(a,r);b=B(b,r);c=A(c,o);d=B(d,o)
  elif v*(r>=b>a):e=A(e,r);f=B(f,r);i=A(i,o);j=B(j,o)
  elif v:L+=[(r,o,v)]
 f=f-e+1;j=j-i+1
 for k in 2,3,4:
  for r in R(a,b-f*k+2):
   for o in R(c,d-j*k+2):
    try:
     for x,y,z in L:1/(g[e+(x-r)//k][i+(y-o)//k]==z)
     for q in R(f*k):g[r+q][o:o+j*k]=[g[e+q//k][i+p//k]for p in R(j*k)]
     return[r[c:d+1]for r in g[a:b+1]]
    except:0