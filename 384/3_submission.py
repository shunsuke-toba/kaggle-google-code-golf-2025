def p(g):y,x=zip(*[(i//9,i%9)for i in range(81)if g[i//9][i%9]]);return[[*sum(zip(r:=g[i//2][min(x):-~max(x)],r),())]for i in range(min(y)*2,-~max(y)*2)]
