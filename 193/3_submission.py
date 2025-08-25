p=lambda g,E=enumerate:[[v*(sum(r[j-(j>0):j+2]+[z[j]for z in g[i-(i>0):i+2]])>v*3)for j,v in E(r)]for i,r in E(g)]
