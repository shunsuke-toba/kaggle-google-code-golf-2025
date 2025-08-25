p=lambda g,z=[0]*10:[[x+u*8+d*2+l*6+r*7 for x,u,d,l,r in zip(a,b,c,[0]+a,a[1:]+[0])]for a,b,c in zip(g,[z]+g,g[1:]+[z])]
