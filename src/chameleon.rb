S="DATA";L=S.split("\0");I={{{chameleon:rand(LANGCOUNT)*FIELDCOUNT}}}{{{ouroboros:LANGINDEXxFIELDCOUNT}}};print L[I]+S.gsub(/[\0\n"\\]/,"\0"=>'\0',"\n"=>'\n','"'=>'\"','\\'=>'\\\\')+L[I+1]
