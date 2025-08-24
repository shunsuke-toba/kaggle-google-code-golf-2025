p=lambda g,e=enumerate:[[v+(i<9)*g[i-9][j]*2+(j<9)*r[j-9]*7+(i>0)*g[i-1][j]*8+(j>0)*r[j-1]*6for j,v in e(r)]for i,r in e(g)]
