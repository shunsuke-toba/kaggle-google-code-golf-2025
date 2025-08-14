def p(g):
 r=[i for i,e in enumerate(g)if 2 in e];v=r[-1]-r[0]>=len(r);v or(g:=[*map(list,zip(*g))],r:=[i for i,e in enumerate(g)if 2 in e])
 h=len(r)//2;a,b=r[0]+h,r[-1]-h
 A=[];B=[]
 for i,R in enumerate(g):
  for j,x in enumerate(R):
   if x==5:R[j]=0;(A if i<a else B).append((i,j))
 for G,e in((sorted(A),a),(sorted(B),b)):
  m,M=G[0][0],G[-1][0];d=e-(M,m)[e==a]
  for y,x in G:g[m+M-y+d][x]=5
 return[g,[*map(list,zip(*g))]][v<1]
