p=lambda g:(t:=max(len({*r})for r in g)>3,c:=[min(s)for r in[g,zip(*g)][t]if(s:={*r}-{0,5})],[c]*len(c)if t else[[v]*len(c)for v in c])[-1]
