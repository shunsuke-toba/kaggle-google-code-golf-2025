p=lambda g,e=enumerate:[[v or g[i-9][j]*2*(i<9)or r[j-9]*7*(j<9)or(i>0)*g[i-1][j]*8+(j>0)*r[j-1]*6for j,v in e(r)]for i,r in e(g)]
