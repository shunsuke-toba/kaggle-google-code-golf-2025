def p(g,R=range):
 c=i=a=e=99;b=d=f=j=0;L=[];m=len(g[0])
 for t in R(len(g)*m):
  if(v:=g[r:=t//m][o:=t%m])&4:b=r;d=o;a>r and(a:=r,c:=o)
  elif v*(a<b<=r):e=min(e,r);f=r;i=min(i,o);j=max(j,o)
  elif v:L+=[(r,o,v)]
 f+=1-e;j+=1-i
 for k in R(5):
  for r in R(a,b):
   for o in R(c,d):
    try:
     for x,y,z in L:1/(g[e+(x-r)//k][i+(y-o)//k]==z)
     for q in R(f*k):g[r+q][o:o+j*k]=[g[e+q//k][i+p//k]for p in R(j*k)]
     return[r[c:d+1]for r in g[a:b+1]]
    except:0