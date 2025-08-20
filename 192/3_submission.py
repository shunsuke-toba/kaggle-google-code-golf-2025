def p(g):
 t=[0]*(len(g[0])+2);G=[t,*[[0]+r+[0]for r in g],t];E=enumerate
 for i,r in E(g):
  for j,v in E(r):
   a,b,c,e=G[i][j+1],G[i+2][j+1],G[i+1][j],G[i+1][j+2];d=sorted((a,b,c,e))
   if v*(v not in d):r[j]=[max(d[::-1],key=d.count),0][a==b!=c==e]
 return g
