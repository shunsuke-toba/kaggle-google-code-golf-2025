def p(g):
 a,b=[i for i,r in enumerate(g)if r[0]>7];c,d=[i for i,v in enumerate(g[0])if v>7];w=d-c-1
 for r in g[:a]:r[c+1:d]=[2]*w
 for r in g[a+1:b]:r[:c]=[4]*c;r[c+1:d]=[6]*w;r[d+1:]=[3]*(len(r)+~d)
 for r in g[b+1:]:r[c+1:d]=[1]*w
 return g
