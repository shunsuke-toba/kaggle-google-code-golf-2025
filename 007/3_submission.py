def p(g):s=sum(g,[]);return[[max(s[(i+j)%3::3])for j in range(7)]for i in range(7)]
