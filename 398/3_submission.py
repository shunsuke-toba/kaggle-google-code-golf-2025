p=lambda g:(a:=g[0],m:=25-5*a.count(0),z:=m*[0],[(z[:m-1-i]+a+z)[:m]for i in range(m)])[-1]
