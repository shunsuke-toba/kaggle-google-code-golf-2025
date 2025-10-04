p=lambda g:exec("""g[:]=map(list,zip(*g[::-1]));a,b,*t=g
for c in t:
 s=bytes(b);k=s.find(8,j:=s.rfind(2))-1
 if-1<j<k:b[j:k+3]=*[2]*(k-j),8,2,8;a[k:k+3]=c[k:k+3]=8,8,8
 a,b=b,c
"""*4)or g