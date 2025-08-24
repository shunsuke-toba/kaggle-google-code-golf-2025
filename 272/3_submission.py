p=lambda g:[[c and-~(sum(r[j-(j>0):j+2]+[k[j]for k in g[i-(i>0):i+2]])>4)for j,c in enumerate(r)]for i,r in enumerate(g)]
