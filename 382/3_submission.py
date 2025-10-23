def p(g):
 a,*_,b=g;t=*map(list,zip(*g)),;d=2in t[0]or-1
 if s:=2in a+b:return*zip(*p(t)),
 for r in(t:=g[::-(a<b)|1]):s+=2in r;r[::d]=r[::d][:s]+t[0][::d][:-s|64]
 return g