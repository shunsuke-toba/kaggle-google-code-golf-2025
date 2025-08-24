def p(g):
 c=g[0].index(8);d=g[0].index(8,c+1);k=0
 for r in g:
  if r[0]:k+=1
  else:r[:]=[k%2*4]*c+[8]+[(2,6,1)[k]]*(d+~c)+[8]+[k%2*3]*(len(r)+~d)
 return g
