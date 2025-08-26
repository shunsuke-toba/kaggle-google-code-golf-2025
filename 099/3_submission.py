p=lambda g,r=range:(h:=[*map(list,g)],[h[a].__setitem__(b,g[a][b]or f)for y in r(10)for x in(0,1,4)if(f:=g[y][x+2])>1 for a in r(y-2-g[y-2][x],y+3-(y>7))for b in r(x,x+5)],h)[2]
