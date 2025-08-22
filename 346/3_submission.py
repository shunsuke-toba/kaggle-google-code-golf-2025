p=lambda g,R=range:next([[b+c]]for i in R(len(g)-2)for j in R(len(g[0])-2)if(b:=g[i][j])*(c:=g[i+1][j+1]-b)and{g[i+u//3][j+u%3]for u in R(9)if u-4}=={b})
