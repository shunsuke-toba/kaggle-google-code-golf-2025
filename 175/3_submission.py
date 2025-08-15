p=lambda g:[[x or g[j][i]or(i==j)*g[0][0]or g[0][1]for j,x in enumerate(r)]for i,r in enumerate(g)]
