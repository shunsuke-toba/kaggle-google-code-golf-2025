def p(g):
 (c,k),*_,(e,w)=[divmod(i,10)for i in range(100)if sum(g,[])[i]]
 for i in-1,1:l=g[c+i];r=g[e+i];l[k+i],r[w+i],l[w-i],r[k-i]=r[w+i],l[k+i],r[k-i],l[w-i]
 return g