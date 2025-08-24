def p(g):
 i=g[0].index;c=i(8);d=i(8,c+1);k=0
 for r in g:
  if r[0]:k+=1
  else:r[:]=[k%2*4]*c+[8]+[(2,6,1)[k]]*(d+~c)+[8]+[k%2*3]*(len(r)+~d)
 return g
