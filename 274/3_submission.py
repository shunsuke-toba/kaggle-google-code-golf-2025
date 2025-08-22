def p(g):s=sum(g,[]);d=(s.index(8)-s.index(5))//len(g[0]);return[([8]*4+[0]*3)[4-d:7-d],[0,0,8*(d>3)],[0]*3]
