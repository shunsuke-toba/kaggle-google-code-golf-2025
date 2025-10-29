def p(q):
 for a in range(19):
  for n in range(19):
   if all(sum(q[a+j][n+i]for i in range(3))for j in range(3))and all(sum(q[a+j][n+i]for j in range(3))for i in range(3)):
    for f in range(3):
     for l in range(3):
      u,g=a,n
      for j in range(3):
       for i in range(3):
        u+=f*4-4;g+=l*4-4
        for j in range(3):
         for i in range(3):
          if q[a+j][n+i]and-1<u+j<21and-1<g+i<21:q[u+j][g+i]=max(q[a+f*4-4+j][n+l*4-4+i]for j in range(3)for i in range(3))
    return q
 return q