def p(g):
 S=Q=[];d=f=p=0
 for r in g:s=sum(r)>>2;S+=Q*s;Q=[(r,s-2,f)]*p*s;d+=s-s*2*f;f^=p>s;p=s
 for r,w,f in S:x=r.index(4)+1;r[x:x+w]=w*[2-(f^(d<0))]
 return g