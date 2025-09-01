def p(g):
 w,r,i=[0]*9,range(11),0
 for v in sum(g,[]):
  if v%5:w[i//44*3+i%11//4]+=1;E=v
  i+=1
 return[[(w[i//4*3+j//4]//max(w)*E,5)[g[i][j]==5]for j in r]for i in r]