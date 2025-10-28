def p(c):
 for x in range(19):
  for g in range(19):
   k=[[c[x+i][g+j]for j in range(3)]for i in range(3)]
   if all(sum(k[i])for i in range(3))and all(sum(k[i][j]for i in range(3))for j in range(3)):
    for w in range(3):
     for l in range(3):
      h=max(c[x+w*4-4+i][g+l*4-4+j]for i in range(3)for j in range(3));y,r=x,g
      for i in range(3):
       for i in range(3):
        y+=w*4-4;r+=l*4-4
        for i in range(3):
         for j in range(3):
          if k[i][j]and-1<y+i<21and-1<r+j<21:c[y+i][r+j]=h
    return c
 return c