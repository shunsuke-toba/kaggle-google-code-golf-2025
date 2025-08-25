p=lambda g,a=range:[[max(g[i//9+x][i%9+y]*(g[i//9+1][i%9+1]==5)for i in a(81))for y in a(3)]for x in a(3)]
