def p(g):
 E=enumerate;f=lambda g:[i for i,e in E(g)if 2 in e];t=lambda z:[*map(list,zip(*z))]
 r=f(g);v=r[-1]-r[0]>len(r);v or(g:=t(g),r:=f(g))
 h=len(r)//2;a,b=r[0]+h,r[-1]-h
 S=[[],[]]
 for i,R in E(g):
  for j,x in E(R):
   if x==5:R[j]=0;S[i>a].append((i,j))
 for G,e in zip(S,(a,b)):
  m=min(G)[0];M=max(G)[0]
  for y,x in G:g[e+[M,m][e>a]-y][x]=5
 return(g,t(g))[v^1]
