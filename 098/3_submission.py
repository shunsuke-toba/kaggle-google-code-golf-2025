p=lambda g:[g[0]]+[[a[0]]+[x*(a[j-1]+a[j+1]+b[j]+c[j]!=4*x)for j,x in enumerate(a[1:-1],1)]+[a[-1]]for a,b,c in zip(g[1:-1],g,g[2:])]+[g[-1]]
