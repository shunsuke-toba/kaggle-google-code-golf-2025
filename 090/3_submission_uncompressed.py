def p(g):
 a,a,b,c,d=max(((max(max(r[c:c+d])for r in g[a:a+b])<1)*b*d,a,b,c,d)for a in range(len(g))for b in range(2,1+len(g)-a)for c in range(len(g[0]))for d in range(2,1+len(g[0])-c))
 for r in g[a:a+b]:r[c:c+d]=[6]*d
 return g