from numpy import*
p=lambda g:(a:=array(g),m:=pad(a==3,1),s:=slice(1,-1),a.__setitem__(m[s,s]&(m[2:,s]|m[:-2,s]|m[s,2:]|m[s,:-2]),8),a.tolist())[4]
