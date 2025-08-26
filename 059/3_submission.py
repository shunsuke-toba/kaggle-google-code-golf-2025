def p(g):
 w,r=[0]*9,range(11);i=0
 for v in sum(g,[]):
  if v%5:w[i//44*3+i%11//4]+=1;E=v
  i+=1
 return[[5*(i%4>2 or j%4>2)or E*(w[i//4*3+j//4]==max(w))for j in r]for i in r]