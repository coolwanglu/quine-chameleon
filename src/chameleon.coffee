P=process;S="DATA";L=S.split '\0';I={{{chameleon:(Math.random()*LANGCOUNT|0)*FIELDCOUNT}}}{{{ouroboros:LANGINDEXxFIELDCOUNT}}};P.stdout.write L[I]+S.replace(/\\/g,'\\\\').replace(/\0/g,'\\0').replace(/\n/g,'\\n').replace(/"/g,'\\"')+L[I+1]

