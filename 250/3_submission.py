def p(g):
 r=0
 while 2 not in g[r]:r+=1
 c=g[r].index(2);o=[[0]*len(g[0])for _ in g]
 for i,R in enumerate(g):
  for j,v in enumerate(R):
   if v>4:o[min(max(i,r-1),r+2)][min(max(j,c-1),c+2)]=5
   if v==2:o[i][j]=2
 return o
