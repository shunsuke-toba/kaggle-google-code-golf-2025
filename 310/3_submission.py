p=lambda g:(s:=sum(g,[]),k:=s.count,c:=min(s,key=k),n:=k(c)//4+1,l:=len(g),i:=s.index(c))and[r[i%l:][:n]for r in g[i//l:][:n]]

