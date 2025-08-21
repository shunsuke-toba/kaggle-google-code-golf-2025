def p(g,r=range(7)):d={i%3:v for i,v in enumerate(sum(g,[]))if v};return[[d[(i+j)%3]for j in r]for i in r]
