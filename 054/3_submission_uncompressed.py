def p(g,R=range):
 for a in R(26):
  for b in R(26):
   v=[g[a+c//5][b+c%5]for c in R(25)]
   if v==v[::-1]and len({*v})>2:
    for c in R(25):g[a+c//5][b+c%5]=v[0]
    for a,b in[(a,b)for a in R(26)for b in R(26)if g[a+2][b+2]==v[12]]:
     for s in 1,-1:
      x,y=a+2,b+2;w=v[12+10*s]
      while w!=v[0]!=g[x][y]:g[x][y]=w;x+=s
     for s in 1,-1:
      x,y=a+2,b+2;w=v[12+2*s]
      while w!=v[0]!=g[x][y]:g[x][y]=w;y+=s
     for c in R(25):
      if v[c]!=v[0]!=g[a+c//5][b+c%5]:g[a+c//5][b+c%5]=v[c]
    return g