p=lambda g,e=enumerate:[g[i+u].__setitem__(j+v,u|v and c*5%9 or c)for i,r in e(g)for j,c in e(r)if c&4<1<c for u in(-1,0,1)for v in(-1,0,1)]and g
