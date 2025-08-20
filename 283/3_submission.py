p=lambda g:[[(r[j],(1,4,2)[sum((j and r[j-1],j<9 and r[j+1],i and g[i-1][j],i<9 and g[i+1][j]))//5-2])[r[j]>4]for j in range(10)]for i,r in enumerate(g)]
