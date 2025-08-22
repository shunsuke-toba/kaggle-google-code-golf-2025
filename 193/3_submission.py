p=lambda g,E=enumerate:[[v*((i and g[i-1][j])+(i+1<len(g)and g[i+1][j])+(j and r[j-1])+(j+1<len(r)and r[j+1])>v)for j,v in E(r)]for i,r in E(g)]
