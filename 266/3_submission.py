def p(g):
 i=sum(g,[]).index(2)*6//5;o=[0]*24;o[i-7]=3;o[i-5]=6;o[i+5]=8;o[i+7]=7;return o[:5],o[6:11],o[12:17]