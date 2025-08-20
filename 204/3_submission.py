def p(g):
 r=range
 for d in r(n:=len(g)):
  for y in r(m:=n-d-1):
   for x in r(m):
    if{g[y][x+i]*g[y+d+1][x+i]*g[y+i][x]*g[y+i][x+d+1]for i in r(d+2)}=={1}:
     for j in g[y+1:y+d+1]:j[x+1:x+d+1]=[2|d%2*5]*d
 return g
