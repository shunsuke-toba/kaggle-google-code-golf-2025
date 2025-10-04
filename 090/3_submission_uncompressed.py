def p(g):
 d,e,c,d=max(((e:=g[a:a+b])and(max(max(r[c:c+d])for r in e)<1)*b*d,e,c,d)for a in range(len(g))for c in range(len(g[0]))for b in range(2,1+len(g)-a)for d in range(2,1+len(g[0])-c))
 for r in e:r[c:c+d]=d*[6]
 return g
