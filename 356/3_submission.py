def p(g):
 r=[x[:]for x in g];L=len;R=range;H=L(g)
 for k in R(H*2):
  t=k//H;i=k%H
  s=[j for j in R(H)if g[i-i*t+j*t][j-j*t+i*t]]
  for j in R(s[0],s[-1]+1)if s else[]:r[i-i*t+j*t][j-j*t+i*t]=8
 return r