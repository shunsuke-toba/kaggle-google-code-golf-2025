p=lambda g:[l:=len(g),b:=[[[r[i:i+3]for r in g],g[i:i+3]][l>3]for i in range(0,[len(g[0]),l][l>3],3)],m:=[[*map(bool,sum(t,[]))]for t in b],b[m.index(min(m,key=m.count))]][3]
