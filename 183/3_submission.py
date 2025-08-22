p=lambda g:(n:=len(g)-4,c:=g[::n+3],r:=range(n),[[c[i>=n/2][-(j>=n/2)]*(g[i+2][j+2]>7)for j in r]for i in r])[-1]
