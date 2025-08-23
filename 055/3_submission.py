def p(g):
 c=g[0].index(8);d=g[0].index(8,c+1);k=0
 for r in g:
  if r[0]:k+=1
  else:r[c+1:d]=[2,6,1][k:k+1]*(d+~c);r[:c]=[k%2*4]*c;r[d+1:]=[k%2*3]*(len(r)+~d)
 return g
