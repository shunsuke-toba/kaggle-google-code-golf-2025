def p(g):
 e=enumerate
 for i,r in e(g):
  for j,c in e(r):
   if c%8 and(i<1 or g[i-1][j]-c)and(j<1 or r[j-1]-c):
    x=j+1
    while x<len(r)and r[x]==c:x+=1
    y=i+1
    while y<len(g)and g[y][j]==c:y+=1
    for z in range(i+1,y-1):g[z][j+1:x-1]=[8]*(x-j-2)
 return g
