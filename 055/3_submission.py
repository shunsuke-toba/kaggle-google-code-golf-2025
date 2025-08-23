def p(g):
 c=g[0].index(8);d=g[0].index(8,c+1);w=d+~c;k=0
 for r in g:
  if r[0]:k+=1;continue
  r[c+1:d]=[2,6,1][k:k+1]*w
  if k%2:r[:c]=[4]*c;r[d+1:]=[3]*(len(r)+~d)
 return g
