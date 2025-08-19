p=lambda g:[[c**(c<1 or c in r[j-1:j]+r[j+1:j+2]+[k[j]for k in g[i-1:i]+g[i+1:i+2]]) for j,c in enumerate(r)]for i,r in enumerate(g)]
