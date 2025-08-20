def p(g):
 b=g[-1];c=len(b)>>1;j=b[c-1]==b[c]==b[c+1];k=j+1
 while~c+k:r=g[-k-2+j];r[c-k]=r[c+k]=b[c];k+=1
 return g
