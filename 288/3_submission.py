def p(g):
 b=g[-1];s=b.index(a:=b[len(b)//2])
 for i in range(s):r=g[i-s-2];r[i]=r[~i]=a
 return g
