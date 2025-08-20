p=lambda g,t=(-1,0,1):[[g[n//9+i].__setitem__(n%9+j,i*j%2*4+abs(i|j))for i in t for j in t]for n,v in enumerate(sum(g,[]))if v]and g
