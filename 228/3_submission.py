def p(g):
 b=[divmod(i,10)for i,v in enumerate(sum(g,[]))if v];c,k=b[0];e,w=b[-1]
 for i in 1,-1:l=g[c+i];r=g[e+i];l[k+i],r[w+i],l[w-i],r[k-i]=r[w+i],l[k+i],r[k-i],l[w-i]
 return g
