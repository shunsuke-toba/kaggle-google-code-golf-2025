def p(g):s=sum(zip(*g),());m=max(map(s.count,range(1,10)));return[[i for i in dict.fromkeys(s) if s.count(i)==m]]*m
