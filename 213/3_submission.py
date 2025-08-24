p=lambda g:(t:=max(len({*r})for r in g)>3,c:=[min(s)for r in[g,zip(*g)][t]if(s:={*r}-{0,5})],h:=[c]*len(c),t and h or[*zip(*h)])[-1]
