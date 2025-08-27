def p(g):b=sum(g,[]);f=b.index;r=f(1);n=[[0]*10for _ in g];[n[(i+r-f(v))//10].__setitem__(i%10,v)for i,v in enumerate(b)if v];return n
