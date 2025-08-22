def p(g):x,=g;c=x.index(0);return[x[:1]*i+x[i:]for i in range(c,c+len(x)//2)]
