def p(g):
 w=[0]*9;R=range(11)
 for i,v in enumerate(sum(g,[])):
  if v%5:w[i//44*3+i%11//4]+=1;E=v
 return[[5*(i%4>2 or j%4>2)or E*(w[i//4*3+j//4]==max(w))for j in R]for i in R]
