def p(g):
 r,c=divmod(sum(g,[]).index(2),10)
 o=[[v&2 for v in r]for r in g]
 for k in range(100):
  if g[i:=k//10][j:=k%10]>4:o[min(max(i,r-1),r+2)][min(max(j,c-1),c+2)]=5
 return o
