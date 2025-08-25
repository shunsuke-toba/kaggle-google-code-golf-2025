def p(g):s=sum(zip(*g),());m=max(map(s.count,{*s}-{0}));return[[i for i in dict.fromkeys(s) if s.count(i)==m]]*m
