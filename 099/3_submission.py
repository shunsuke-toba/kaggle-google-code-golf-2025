p=lambda g,r=range:(h:=[*map(list,g)],[[h[y].__setitem__(X,g[y][X]or f)for y in r(y-2-g[y-2][x],y+3-(y>7))for X in r(x,x+5)]for i in r(60)if(f:=g[(y:=i//6)][(x:=i%6)+2])>1],h)[2]
