def p(g,F=filter):
 s=sum(g,[]);f=lambda r:min({*s}-{0},key=s.count)in r;return[*map(list,zip(*F(f,zip(*F(f,g)))))]