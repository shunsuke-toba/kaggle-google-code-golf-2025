def p(g,R=range):
 h,w=len(g),len(g[0])
 for s in R(3,6):
  c=s+3
  for i in R(h-s+1):
   for j in R(w-s+1):
    k=j+s-1;l=i+s-1
    if g[i][j:j+s]==[5]*s==g[l][j:j+s]and all(g[y][j]==g[y][k]==5 for y in R(i,l+1)):
     for y in R(i+1,l):g[y][j+1:k]=[c]*(s-2)
 return g