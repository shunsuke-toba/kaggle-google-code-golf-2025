def p(g):
 S=Q=[];j=1;d=p=0
 for r in g:s=sum(r)>>2;S+=Q[:s];Q=[(r,s-2,j)][:p*s];p>s and(j:=-j);d+=s*j;p=s
 for r,w,j in S:x=r.index(4)+1;r[x:x+w]=w*[1+(j*d>0)]
 return g