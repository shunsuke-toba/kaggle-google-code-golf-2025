R=range
def p(g):
 r=[*map(list,g)];m=len(g);n=len(g[0])
 for y in R(m):
  for x in R(n):
   if g[y][x]==6 and (y<1 or g[y-1][x]-6) and (x<1 or g[y][x-1]-6):
    w=h=1
    while x+w<n and g[y][x+w]==6:w+=1
    while y+h<m and g[y+h][x]==6:h+=1
    for i in R(y+1,y+h-1):r[i][x+1:x+w-1]=[(c,4)[c>7]for c in r[i][x+1:x+w-1]]
 for y in R(m):
  for x in R(n):
   if r[y][x]>7 and any(m>i>=0<=j<n and r[i][j]==6 for i in R(y-1,y+2) for j in R(x-1,x+2)):r[y][x]=3
 return r
