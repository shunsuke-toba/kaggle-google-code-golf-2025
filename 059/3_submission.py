def p(g):
 w,r=[0]*9,range(11)
 for i,v in enumerate(sum(g,[])):
  if v%5:w[i//44*3+i%11//4]+=1;E=v
 return[[5*(g[i][j]==5)or w[i//4*3+j//4]//max(w)*E for j in r]for i in r]