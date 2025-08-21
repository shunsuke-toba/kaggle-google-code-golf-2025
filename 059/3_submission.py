def p(g):
 w=[0]*9;R=range(11)
 for i,v in enumerate(sum(g,[])):
  w[i//44*3+i%11//4]+=v%5>0;v%5 and(E:=v)
 m=max(w);return[[5*(i%4>2 or j%4>2)or E*(w[i//4*3+j//4]==m)for j in R]for i in R]
