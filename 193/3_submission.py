p=lambda g,E=enumerate:[[v*((i>0)*g[i-1][j]+(i+1<len(g)and g[i+1][j])+(j>0)*r[j-1]+(r[j+1:j+2]+[0])[0]>v)for j,v in E(r)]for i,r in E(g)]
