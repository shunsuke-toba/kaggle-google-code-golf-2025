p=lambda g,e=enumerate:[[v or i<9and g[i+1][j]*2or j<9and r[j+1]*7or(i>0)*g[i-1][j]*8+(j>0)*r[j-1]*6for j,v in e(r)]for i,r in e(g)]
