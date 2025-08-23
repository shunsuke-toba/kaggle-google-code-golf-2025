p=lambda g:(t:=any(len({*r})>3 for r in g),g:=[*zip(*g)]if t else g,c:=[min(s)for r in g if(s:={*r}-{0,5})],[c]*len(c) if t else[[v]*len(c) for v in c])[-1]
