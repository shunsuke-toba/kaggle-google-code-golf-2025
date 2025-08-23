def p(g):
 s=[(1,0),(4,5)]if 4 not in g[8]else[(1,2),(6,5)]
 for r,c in s:
  for i in 0,1,2:g[r+i][c:c+3]=[v or 7 for v in g[r+i][c:c+3]]
 return g
