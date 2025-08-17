from numpy import*
def p(g):g=array(g);s=sum(~all(g-2,1))-2;y,x=where(g%2+g//3);u,v=y.min(),x.min();h,w=ptp(y)+1,ptp(x)+1;return pad(kron(g[u:u+h,v:v+w],ones((s//h,s//w))),1,constant_values=2).tolist()
