def p(g):
 for i in range(11):
  for j in range(11):
   for k in range(11):
    u=g[i:i+k+2]
    if not(sum(sum(r[j:j+k+2])for r in u)-20*-~k|sum(sum(r[j+1:j+k+1])for r in u[1:-1])):
     for r in u[1:-1]:r[j+1:j+k+1]=[2]*k
 return g
