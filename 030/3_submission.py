def p(g):b=bytes(sum(g,[]));f=b.rfind;r=f(1)//10;n=[[0]*10for _ in g];[n[k//10+r-f(v)//10].__setitem__(k%10,v)for k,v in enumerate(b)if v];return n
