S="DATA";L=S.split("\t");I={{{chameleon:rand(LANGCOUNT)*FIELDCOUNT}}}{{{ouroboros:ENTRYINDEX}}};print L[I]+S.gsub(/[\t\n"\\]/,"\t"=>'\t',"\n"=>'\n','"'=>'\"','\\'=>'\\\\')+L[I+1]
