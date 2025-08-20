def p(g):
 w=[0]*9
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if 0<v!=5:w[y//4*3+x//4]+=1;E=v
 m=max(w);R=range(11)
 return [[5*(i%4==3 or j%4==3) or E*(w[i//4*3+j//4]==m) for j in R]for i in R]
