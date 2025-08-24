p=lambda g,E=enumerate:[[v*(g[i-1][j]*(i>0)+(i+1<len(g)and g[i+1][j])+sum(r[j-(j>0):j+2])-v>v)for j,v in E(r)]for i,r in E(g)]
