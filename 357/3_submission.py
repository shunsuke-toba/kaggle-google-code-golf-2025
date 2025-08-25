def p(g):
 c=d=0
 for r in g[::-1]:w=len(r);r[:]=[8]*w;r[c]=1;c+=1-2*d;d^=c%(w-1)<1
 return g