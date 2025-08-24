p=lambda g:[g[n//9+i].__setitem__(n%9+j,(i|j)%2+i*j*4%8)for n,v in enumerate(sum(g,[]))if v for i in(-1,0,1)for j in(-1,0,1)]and g
