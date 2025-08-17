p=lambda g,E=enumerate:[[v*((i and g[i-1][j]>0)+(i+1<len(g)and g[i+1][j]>0)+(j and r[j-1]>0)+(j+1<len(r)and r[j+1]>0)>1)for j,v in E(r)]for i,r in E(g)]
