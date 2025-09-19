def p(g,z=63):
 a,b,c,*_=g[z>>3:]
 if min(a[s:=slice(z%8,z%8+3)]+c[s]):a[s]=c[s]=0,2,0;b[s]=2,2,2
 if z:p(g,z-1);return g