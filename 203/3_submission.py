p=lambda j:(n:=len(j),R:=range(n))and[[j[k:=n//2-min(x+1,y+1,n-x,n-y)][k]for y in R]for x in R]
