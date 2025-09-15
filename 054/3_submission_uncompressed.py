def p(g,R=range):
 for a in R(26):
  for b in R(26):
   v=[g[a+c//5][b+c%5]for c in R(25)]
   if v==v[::-1]and len({*v})>2:
    z=v[0]
    for c in R(25):g[a+c//5][b+c%5]=z
    for a,b in[(a+2,b+2)for a in R(26)for b in R(26)if g[a+2][b+2]==v[12]]:
     x,y=a,b;w=v[22]
     while w!=z!=g[x][y]:g[x][y]=w;x+=1
     x,y=a,b;w=v[10]
     while w!=z!=g[x][y]:g[x][y]=w;y+=1
     x,y=a,b;w=v[2]
     while w!=z!=g[x][y]:g[x][y]=w;x-=1
     x,y=a,b;w=v[14]
     while w!=z!=g[x][y]:g[x][y]=w;y-=1
     for c in R(25):
      if g[a-2+c//5][b-2+c%5]!=z!=v[c]:g[a-2+c//5][b-2+c%5]=v[c]
    return g
