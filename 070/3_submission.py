def p(g):
 a=b=0
 for k in zip(*g):b+=8in k;a+=b<1
 for r in g:r[a:a+b]=[x|x+(8in r)&2for x in r[a:a+b]]
 return g