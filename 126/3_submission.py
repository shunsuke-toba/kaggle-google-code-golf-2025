p=lambda g:([g[-1].__setitem__(x,4)for u,r in zip(g,g[1:])for x in range(1,len(r)-1)if u[x]==r[x-1]==r[x+1]!=r[x]],g)[1]
