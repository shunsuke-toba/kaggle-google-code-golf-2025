def p(a):
 b=[(i//10,i%10)for i in range(100)if a[i//10][i%10]];c,k=b[0];e,w=b[-1]
 for i in 1,-1:a[c+i][k+i],a[e+i][w+i],a[c+i][w-i],a[e+i][k-i]=a[e+i][w+i],a[c+i][k+i],a[e+i][k-i],a[c+i][w-i]
 return a
