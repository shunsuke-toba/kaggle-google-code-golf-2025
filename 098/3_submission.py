p=lambda g:g[:1]+[[0]+[x*(b[j-1]+b[j+1]+a[j]+c[j]!=4*x)for j,x in enumerate(b[1:-1],1)]+[0]for a,b,c in zip(g,g[1:],g[2:])]+g[:1]
