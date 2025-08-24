p=lambda g,e=enumerate:[g[i+u].__setitem__(j+v,(c,c*5%9)[u|v])for i,r in e(g)for j,c in e(r)if c%6&2 for u in(-1,0,1)for v in(-1,0,1)]and g
