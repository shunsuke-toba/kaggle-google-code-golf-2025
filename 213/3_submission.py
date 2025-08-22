p=lambda g:(t:=any(len({v for v in r if v%5})>1 for r in g),g:=[*zip(*g)]if t else g,c:=[next(v for v in r if v%5)for r in g if any(v%5 for v in r)],[c]*len(c) if t else[[v]*len(c) for v in c])[-1]
