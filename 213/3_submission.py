p=lambda g:(t:=max(len({*r})for r in g)<4,c:=[s.pop()for r in[zip(*g),g][t]if(s:={*r}-{0,5})],h:=[c]*len(c))and[h,[*zip(*h)]][t]
